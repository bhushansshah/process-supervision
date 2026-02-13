"""System prompts for TIR reasoning and critique."""

from __future__ import annotations

# ---------------------------------------------------------------------------
# TIR (Tool-Integrated Reasoning) system prompts
# ---------------------------------------------------------------------------

QWEN_TIR_SYSTEM = (
    "Please integrate natural language reasoning with programs to solve the "
    "problem above, and put your final answer within \\boxed{}."
)

DEEPSEEK_TIR_SYSTEM = (
    "Please reason step by step, and put your final answer within \\boxed{}.\n"
    "You can use Python code blocks to help with calculations. "
    "Write code in ```python ... ``` blocks and the execution result will be "
    "provided to you."
)

# Default fallback
DEFAULT_TIR_SYSTEM = QWEN_TIR_SYSTEM

# ---------------------------------------------------------------------------
# Critique prompt
# ---------------------------------------------------------------------------

CRITIQUE_SYSTEM = """\
You are a careful mathematical reasoning verifier. Your job is to check whether
the latest reasoning step is correct, given the problem and all prior reasoning.

Analyze the step for:
1. Logical correctness — does the conclusion follow from the premises?
2. Computational accuracy — are arithmetic / algebraic manipulations correct?
3. Completeness — are there missing cases or unjustified leaps?

Respond in EXACTLY this format (do NOT deviate):

CORRECT: <yes or no>
ERROR: <one-sentence description of the error, or "none">
SUGGESTION: <one-sentence suggestion for fixing the error, or "none">
"""

CRITIQUE_USER_TEMPLATE = """\
## Problem
{problem}

## Reasoning so far
{reasoning_so_far}

## Current step to verify
{current_step}

Verify the current step.
"""

# ---------------------------------------------------------------------------
# Code output formatting
# ---------------------------------------------------------------------------


def format_code_output(stdout: str, error: str | None = None) -> str:
    """Format the execution result to inject back into the conversation."""
    if error:
        return f"```output\n{error}\n```"
    return f"```output\n{stdout}\n```"


def format_critique_feedback(is_correct: bool, error_desc: str, suggestion: str) -> str:
    """Format critique feedback to inject into the model's context."""
    if is_correct:
        return ""
    return f"[Critique]: Error detected — {error_desc}. Suggestion: {suggestion}"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

MODEL_SYSTEM_PROMPTS: dict[str, str] = {
    "qwen": QWEN_TIR_SYSTEM,
    "deepseek": DEEPSEEK_TIR_SYSTEM,
}


def get_system_prompt(model_name: str) -> str:
    """Return the appropriate TIR system prompt for the given model name."""
    name_lower = model_name.lower()
    for key, prompt in MODEL_SYSTEM_PROMPTS.items():
        if key in name_lower:
            return prompt
    return DEFAULT_TIR_SYSTEM
