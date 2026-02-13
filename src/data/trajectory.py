"""Pydantic models for step-level trajectory data."""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class StepType(Enum):
    """Type of a single step in a reasoning trajectory."""

    REASONING = "reasoning"
    CODE = "code"
    CODE_OUTPUT = "code_output"
    CRITIQUE = "critique"
    ANSWER = "answer"


class CritiqueResult(BaseModel):
    """Structured output from the critique tool."""

    is_correct: bool = True
    error_description: str = "none"
    suggestion: str = "none"


class Step(BaseModel):
    """A single step in a trajectory."""

    step_idx: int
    step_type: StepType
    content: str
    critique_result: Optional[CritiqueResult] = None
    # For PRM labeling (populated during annotation, not during generation)
    label: Optional[float] = None  # correctness score 0-1

    class Config:
        use_enum_values = True


class Trajectory(BaseModel):
    """Complete trajectory for one problem."""

    problem: str
    ground_truth: str = ""
    steps: list[Step] = Field(default_factory=list)
    final_answer: Optional[str] = None
    is_correct: bool = False
    model_name: str = ""
    metadata: dict = Field(default_factory=dict)

    def add_step(self, step: Step) -> None:
        """Append a step to the trajectory."""
        self.steps.append(step)

    @property
    def num_reasoning_steps(self) -> int:
        return sum(1 for s in self.steps if s.step_type == StepType.REASONING.value)

    @property
    def num_code_steps(self) -> int:
        return sum(1 for s in self.steps if s.step_type == StepType.CODE.value)

    @property
    def num_critique_steps(self) -> int:
        return sum(1 for s in self.steps if s.step_type == StepType.CRITIQUE.value)

    def to_jsonl_dict(self) -> dict:
        """Serialize to a dict suitable for JSONL export."""
        return self.model_dump()
