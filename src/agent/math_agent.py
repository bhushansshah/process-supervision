"""Math-specific orchestrator — convenience wrapper around AgentLoop."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

from src.agent.base import AgentLoop
from src.backend.vllm_client import VLLMClient
from src.config import AgentConfig
from src.data.trajectory import Trajectory
from src.tools.critique import CritiqueTool
from src.tools.python_interpreter import PythonInterpreter

logger = logging.getLogger(__name__)


class MathAgent:
    """High-level interface for solving math problems.

    Handles setup of the vLLM client, tools, and the agent loop so that
    callers only need to pass a config and call :meth:`solve`.
    """

    def __init__(self, config: AgentConfig) -> None:
        self.config = config
        self._client: Optional[VLLMClient] = None
        self._loop: Optional[AgentLoop] = None

    async def setup(self) -> None:
        """Initialize the client, tools, and agent loop."""
        self._client = VLLMClient(self.config.model)

        # Python interpreter
        python_interp: Optional[PythonInterpreter] = None
        if self.config.python_tool.enabled:
            python_interp = PythonInterpreter(
                timeout=self.config.python_tool.timeout_seconds,
                allowed_modules=self.config.python_tool.allowed_modules,
            )

        # Critique tool
        critique: Optional[CritiqueTool] = None
        if self.config.critique.enabled:
            critique_client = self._client  # reuse by default
            if self.config.critique.model is not None:
                critique_client = VLLMClient(self.config.critique.model)
            critique = CritiqueTool(critique_client, self.config.generation)

        self._loop = AgentLoop(
            config=self.config,
            vllm_client=self._client,
            python_interpreter=python_interp,
            critique_tool=critique,
        )

    async def solve(self, problem: str, ground_truth: Optional[str] = None) -> Trajectory:
        """Solve a single math problem.

        Args:
            problem: Problem statement text.
            ground_truth: Optional correct answer for trajectory labeling.

        Returns:
            Full trajectory with steps and final answer.
        """
        if self._loop is None:
            await self.setup()
        assert self._loop is not None
        return await self._loop.solve(problem, ground_truth)

    async def close(self) -> None:
        """Clean up resources."""
        if self._client is not None:
            await self._client.close()

    async def __aenter__(self) -> "MathAgent":
        await self.setup()
        return self

    async def __aexit__(self, *exc) -> None:
        await self.close()

    @classmethod
    def from_yaml(cls, path: str | Path) -> "MathAgent":
        """Create a MathAgent from a YAML config file."""
        config = AgentConfig.from_yaml(path)
        return cls(config)
