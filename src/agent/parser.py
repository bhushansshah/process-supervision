"""Parse model output to detect code blocks, boxed answers, and reasoning steps."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class ChunkType(Enum):
    REASONING = "reasoning"
    CODE = "code"
    ANSWER = "answer"


@dataclass
class ParsedChunk:
    """A single parsed segment of model output."""

    chunk_type: ChunkType
    content: str
    # For CODE chunks, the raw code inside the block
    code: Optional[str] = None
    # For ANSWER chunks, the extracted boxed answer
    boxed_answer: Optional[str] = None


# ---------------------------------------------------------------------------
# Regex patterns
# ---------------------------------------------------------------------------

# Match ```python ... ``` blocks (greedy within a single generation chunk)
_CODE_BLOCK_RE = re.compile(
    r"```python\s*\n(.*?)(?:```|$)",
    re.DOTALL,
)

# Match \boxed{...} with proper brace nesting
_BOXED_RE = re.compile(r"\\boxed\{")


def _extract_boxed(text: str) -> Optional[str]:
    """Extract content from the first \\boxed{...} in *text*, handling nested braces."""
    m = _BOXED_RE.search(text)
    if m is None:
        return None
    start = m.end()  # right after the opening brace
    depth = 1
    i = start
    while i < len(text) and depth > 0:
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
        i += 1
    if depth != 0:
        # Unbalanced — return what we have
        return text[start: i].strip()
    return text[start: i - 1].strip()


def has_code_block(text: str) -> bool:
    """Return True if *text* contains a ```python code block."""
    return "```python" in text


def extract_code(text: str) -> Optional[str]:
    """Return the code inside the first ```python block, or None."""
    m = _CODE_BLOCK_RE.search(text)
    if m:
        return m.group(1).strip()
    # If the block was not closed (model stopped at stop sequence), grab
    # everything after the marker.
    idx = text.find("```python")
    if idx != -1:
        code = text[idx + len("```python"):].strip()
        # Remove trailing ``` if present
        if code.endswith("```"):
            code = code[:-3].strip()
        return code if code else None
    return None


def has_boxed_answer(text: str) -> bool:
    """Return True if *text* contains \\boxed{...}."""
    return _BOXED_RE.search(text) is not None


def extract_boxed_answer(text: str) -> Optional[str]:
    """Extract the content of the first \\boxed{...} in *text*."""
    return _extract_boxed(text)


def parse_response(text: str) -> list[ParsedChunk]:
    """Parse a full model response into a list of typed chunks.

    The output list preserves ordering.  For each segment we emit one of:
    - REASONING — plain text / natural-language reasoning
    - CODE — a ```python block (with .code populated)
    - ANSWER — a segment containing \\boxed{} (with .boxed_answer populated)
    """
    chunks: list[ParsedChunk] = []
    remaining = text

    while remaining:
        # 1. Try to find the next code block
        code_match = _CODE_BLOCK_RE.search(remaining)
        code_start = remaining.find("```python") if code_match is None else code_match.start()

        if code_match is not None:
            # Everything before the code block is reasoning
            before = remaining[: code_match.start()].strip()
            if before:
                _emit_reasoning_or_answer(before, chunks)
            chunks.append(
                ParsedChunk(
                    chunk_type=ChunkType.CODE,
                    content=code_match.group(0),
                    code=code_match.group(1).strip(),
                )
            )
            remaining = remaining[code_match.end():].strip()
        else:
            # No code block found — rest is reasoning / answer
            _emit_reasoning_or_answer(remaining, chunks)
            break

    return chunks


def split_reasoning_steps(text: str) -> list[str]:
    """Split reasoning text into individual steps on double newlines or 'Step N:' markers."""
    # First try explicit step markers
    step_parts = re.split(r"\n(?=Step\s+\d+)", text)
    if len(step_parts) > 1:
        return [p.strip() for p in step_parts if p.strip()]
    # Fall back to double newline splitting
    parts = re.split(r"\n\s*\n", text)
    return [p.strip() for p in parts if p.strip()]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _emit_reasoning_or_answer(text: str, chunks: list[ParsedChunk]) -> None:
    """Append a REASONING or ANSWER chunk depending on whether \\boxed{} is present."""
    boxed = _extract_boxed(text)
    if boxed is not None:
        chunks.append(
            ParsedChunk(chunk_type=ChunkType.ANSWER, content=text, boxed_answer=boxed)
        )
    else:
        chunks.append(ParsedChunk(chunk_type=ChunkType.REASONING, content=text))
