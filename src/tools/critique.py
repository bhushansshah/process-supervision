"""LLM-based critique tool for verifying reasoning steps."""

from __future__ import annotations

import logging
import re
from typing import Optional

from src.agent.prompts import CRITIQUE_SYSTEM, CRITIQUE_USER_TEMPLATE
from src.backend.vllm_client import VLLMClient
from src.config import GenerationConfig
from src.data.trajectory import CritiqueResult

logger = logging.getLogger(__name__)


class CritiqueTool:
    """Send a reasoning step to an LLM for verification.

    Makes a separate LLM call with a critique-specific system prompt and
    returns structured feedback.
    """

    def __init__(
        self,
        client: VLLMClient,
        generation_config: Optional[GenerationConfig] = None,
    ) -> None:
        self.client = client
        self.gen_config = generation_config or GenerationConfig(
            temperature=0.0,
            max_tokens=256,
            stop_sequences=[],
        )

    async def analyze(
        self,
        problem: str,
        reasoning_so_far: str,
        current_step: str,
    ) -> CritiqueResult:
        """Critique the *current_step* given the full context.

        Args:
            problem: Original problem statement.
            reasoning_so_far: All prior reasoning / code / outputs concatenated.
            current_step: The specific step to verify.

        Returns:
            A :class:`CritiqueResult` with structured feedback.
        """
        user_msg = CRITIQUE_USER_TEMPLATE.format(
            problem=problem,
            reasoning_so_far=reasoning_so_far,
            current_step=current_step,
        )

        messages = [
            {"role": "system", "content": CRITIQUE_SYSTEM},
            {"role": "user", "content": user_msg},
        ]

        # Use a separate generation config for critique (no code-block stop) #TODO: this seems to be redundant.
        critique_gen = GenerationConfig(
            temperature=self.gen_config.temperature,
            top_p=self.gen_config.top_p,
            max_tokens=256,
            stop_sequences=[],
        )

        try:
            response = await self.client.generate(
                messages=messages,
                generation_config=critique_gen,
            )
            return self._parse_response(response)
        except Exception:
            logger.exception("Critique call failed")
            # On failure, assume the step is correct to avoid blocking the agent
            return CritiqueResult(
                is_correct=True,
                error_description="Critique unavailable",
                suggestion="none",
            )

    @staticmethod
    def _parse_response(text: str) -> CritiqueResult:
        """Parse the structured critique response into a :class:`CritiqueResult`."""
        is_correct = True
        error_description = "none"
        suggestion = "none"

        for line in text.strip().splitlines():
            line_stripped = line.strip()
            upper = line_stripped.upper()

            if upper.startswith("CORRECT:"):
                value = line_stripped.split(":", 1)[1].strip().lower()
                is_correct = value in ("yes", "true", "correct")

            elif upper.startswith("ERROR:"):
                error_description = line_stripped.split(":", 1)[1].strip()

            elif upper.startswith("SUGGESTION:"):
                suggestion = line_stripped.split(":", 1)[1].strip()

        return CritiqueResult(
            is_correct=is_correct,
            error_description=error_description,
            suggestion=suggestion,
        )
