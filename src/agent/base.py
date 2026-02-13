"""Core agent loop: generate → parse → execute → observe."""

from __future__ import annotations

import logging
from typing import Optional

from src.agent.parser import (
    ChunkType,
    extract_boxed_answer,
    extract_code,
    has_boxed_answer,
    has_code_block,
    parse_response,
    split_reasoning_steps,
)
from src.agent.prompts import format_code_output, format_critique_feedback, get_system_prompt
from src.backend.vllm_client import VLLMClient
from src.config import AgentConfig
from src.data.trajectory import CritiqueResult, Step, StepType, Trajectory
from src.tools.critique import CritiqueTool
from src.tools.python_interpreter import PythonInterpreter

logger = logging.getLogger(__name__)


class AgentLoop:
    """TIR agent loop that coordinates generation, code execution, and critique.

    The loop repeats until the model emits a ``\\boxed{}`` answer or the
    maximum number of turns is reached.
    """

    def __init__(
        self,
        config: AgentConfig,
        vllm_client: VLLMClient,
        python_interpreter: Optional[PythonInterpreter] = None,
        critique_tool: Optional[CritiqueTool] = None,
    ) -> None:
        self.config = config
        self.client = vllm_client

        # Tools
        self.python = python_interpreter or (
            PythonInterpreter(timeout=config.python_tool.timeout_seconds)
            if config.python_tool.enabled
            else None
        )
        self.critique = critique_tool  # may be None

        # Determine system prompt from model name
        self.system_prompt = get_system_prompt(config.model.name)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    async def solve(self, problem: str, ground_truth: Optional[str] = None) -> Trajectory:
        """Run the agent on a single math problem and return the full trajectory.

        Args:
            problem: The math problem text.
            ground_truth: Optional known correct answer (used for trajectory labeling only).

        Returns:
            A :class:`Trajectory` recording every step.
        """
        trajectory = Trajectory(
            problem=problem,
            ground_truth=ground_truth or "",
            model_name=self.config.model.name,
        )

        # Build the initial message list
        messages: list[dict] = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": problem},
        ]

        turn = 0
        step_idx = 0
        final_answer: Optional[str] = None

        while turn < self.config.max_turns:
            turn += 1
            logger.info("Turn %d / %d", turn + 1, self.config.max_turns)

            # 1. THINK — generate next reasoning chunk
            response_text = await self.client.generate(
                messages=messages,
                generation_config=self.config.generation,
            )

            # Parse the response into chunks
            chunks = parse_response(response_text)

            for chunk in chunks:
                if chunk.chunk_type == ChunkType.REASONING:
                    # Log reasoning steps
                    reasoning_steps = split_reasoning_steps(chunk.content)
                    for r_step in reasoning_steps:
                        trajectory.add_step(Step(
                            step_idx=step_idx,
                            step_type=StepType.REASONING,
                            content=r_step,
                        ))
                        step_idx += 1

                elif chunk.chunk_type == ChunkType.CODE:
                    # Log the code step
                    trajectory.add_step(Step(
                        step_idx=step_idx,
                        step_type=StepType.CODE,
                        content=chunk.code or "",
                    ))
                    step_idx += 1

                elif chunk.chunk_type == ChunkType.ANSWER:
                    trajectory.add_step(Step(
                        step_idx=step_idx,
                        step_type=StepType.ANSWER,
                        content=chunk.content,
                    ))
                    step_idx += 1
                    final_answer = chunk.boxed_answer

            # Append raw assistant response to messages
            messages.append({"role": "assistant", "content": response_text})

            # 2. Check for final answer
            if final_answer is not None:
                logger.info("Final answer found: %s", final_answer)
                break

            # 3. ACT — execute code if present
            if has_code_block(response_text) and self.python is not None:
                code = extract_code(response_text)
                if code:
                    stdout, error = self.python.execute(code)
                    output_text = format_code_output(stdout, error)

                    # Log code output
                    trajectory.add_step(Step(
                        step_idx=step_idx,
                        step_type=StepType.CODE_OUTPUT,
                        content=output_text,
                    ))
                    step_idx += 1

                    # Inject output back into the conversation
                    messages.append({"role": "user", "content": output_text})

            # 4. CRITIQUE — optionally critique the latest reasoning
            critique_result = await self._maybe_critique(
                problem, trajectory, step_idx, turn
            )
            if critique_result is not None and not critique_result.is_correct:
                feedback = format_critique_feedback(
                    critique_result.is_correct,
                    critique_result.error_description,
                    critique_result.suggestion,
                )
                trajectory.add_step(Step(
                    step_idx=step_idx,
                    step_type=StepType.CRITIQUE,
                    content=feedback,
                    critique_result=critique_result,
                ))
                step_idx += 1
                messages.append({"role": "user", "content": feedback})

        # Finalize trajectory
        trajectory.final_answer = final_answer
        if ground_truth and final_answer:
            trajectory.is_correct = self._check_answer(final_answer, ground_truth)
        else:
            trajectory.is_correct = False

        return trajectory

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    async def _maybe_critique(
        self,
        problem: str,
        trajectory: Trajectory,
        step_idx: int,
        turn: int,
    ) -> Optional[CritiqueResult]:
        """Run the critique tool if it's enabled and due this turn."""
        if self.critique is None or not self.config.critique.enabled:
            return None

        # Check frequency
        freq = self.config.critique.frequency
        if freq <= 0:
            return None

        # Check after_code_only constraint
        if self.config.critique.after_code_only:
            # Only run if the last step was a code output
            if trajectory.steps and trajectory.steps[-1].step_type != StepType.CODE_OUTPUT:
                return None
        elif turn % freq != 0:
            return None

        # Build reasoning-so-far text
        reasoning_so_far = "\n\n".join(
            f"[{s.step_type.value}] {s.content}" for s in trajectory.steps
        )
        # Current step = last step
        current_step = trajectory.steps[-1].content if trajectory.steps else ""

        return await self.critique.analyze(
            problem=problem,
            reasoning_so_far=reasoning_so_far,
            current_step=current_step,
        )

    @staticmethod
    def _check_answer(predicted: str, ground_truth: str) -> bool:
        """Simple string-based answer comparison (evaluation module has the full version)."""
        return predicted.strip().lower() == ground_truth.strip().lower()
