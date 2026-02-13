"""Pydantic settings for the math reasoning agent."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel, Field


class GenerationConfig(BaseModel):
    """Parameters for LLM text generation."""

    temperature: float = 0.0
    top_p: float = 1.0
    max_tokens: int = 2048
    stop_sequences: list[str] = Field(default_factory=lambda: ["```output"])
    # When we detect `python\n`, we let the model keep generating until it
    # closes the code block; then we stop on "```\n" or "```output" to inject
    # the execution result.


class ModelConfig(BaseModel):
    """Configuration for a single model served by vLLM."""

    name: str = "Qwen/Qwen2.5-Math-7B-Instruct"
    api_base: str = "http://localhost:8000/v1"
    api_key: str = "EMPTY"
    served_model_name: Optional[str] = None  # --served-model-name override

    @property
    def effective_name(self) -> str:
        return self.served_model_name or self.name


class CritiqueConfig(BaseModel):
    """Configuration for the LLM-based critique tool."""

    enabled: bool = True
    frequency: int = 1  # critique every N steps (0 = only after code)
    after_code_only: bool = False
    model: Optional[ModelConfig] = None  # None → reuse reasoning model


class PythonToolConfig(BaseModel):
    """Configuration for the Python interpreter tool."""

    enabled: bool = True
    timeout_seconds: int = 30
    allowed_modules: list[str] = Field(
        default_factory=lambda: ["sympy", "math", "numpy", "fractions", "itertools", "functools", "collections"]
    )


class AgentConfig(BaseModel):
    """Top-level agent configuration."""

    model: ModelConfig = Field(default_factory=ModelConfig)
    generation: GenerationConfig = Field(default_factory=GenerationConfig)
    critique: CritiqueConfig = Field(default_factory=CritiqueConfig)
    python_tool: PythonToolConfig = Field(default_factory=PythonToolConfig)
    max_turns: int = 15
    max_context_tokens: int = 3800  # stay under 4K context window
    output_dir: str = "results"

    @classmethod
    def from_yaml(cls, path: str | Path) -> "AgentConfig":
        """Load configuration from a YAML file."""
        with open(path) as f:
            raw = yaml.safe_load(f)
        return cls.model_validate(raw)
