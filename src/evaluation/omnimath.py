"""Load and iterate over the Omni-MATH dataset from HuggingFace."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Iterator, Optional

from datasets import load_dataset

logger = logging.getLogger(__name__)

DATASET_NAME = "KbsdJames/Omni-MATH"


@dataclass
class MathProblem:
    """A single problem from the Omni-MATH dataset."""

    idx: int
    question: str
    answer: str
    solution: str
    domain: str
    difficulty: str


def load_omnimath(
    split: str = "test",
    domain: Optional[str] = None,
    difficulty: Optional[str] = None,
    max_problems: Optional[int] = None,
) -> list[MathProblem]:
    """Load Omni-MATH problems from HuggingFace.

    Args:
        split: Dataset split to use (default "test").
        domain: Filter by domain (e.g. "algebra", "geometry"). None = all.
        difficulty: Filter by difficulty level. None = all.
        max_problems: Maximum number of problems to load. None = all.

    Returns:
        List of :class:`MathProblem` instances.
    """
    logger.info("Loading Omni-MATH dataset (split=%s)...", split)
    ds = load_dataset(DATASET_NAME, split=split)
    logger.info("Loaded %d raw problems", len(ds))

    problems: list[MathProblem] = []
    for idx, row in enumerate(ds):
        # Apply filters
        row_domain = row.get("domain", "")
        row_difficulty = row.get("difficulty", "")

        if domain and domain.lower() not in row_domain.lower():
            continue
        if difficulty and difficulty.lower() not in row_difficulty.lower():
            continue

        problems.append(MathProblem(
            idx=idx,
            question=row["question"],
            answer=row.get("answer", ""),
            solution=row.get("solution", ""),
            domain=row_domain,
            difficulty=row_difficulty,
        ))

        if max_problems and len(problems) >= max_problems:
            break

    logger.info(
        "Selected %d problems (domain=%s, difficulty=%s, max=%s)",
        len(problems), domain, difficulty, max_problems,
    )
    return problems


def iterate_problems(
    problems: list[MathProblem],
) -> Iterator[MathProblem]:
    """Simple iterator for use in evaluation loops."""
    yield from problems
