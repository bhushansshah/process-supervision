"""Evaluation metrics: accuracy, per-category breakdown, step-level stats."""

from __future__ import annotations

import json
import logging
from collections import defaultdict
from pathlib import Path
from typing import Optional

from src.data.trajectory import Trajectory

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Core metrics
# ---------------------------------------------------------------------------

def compute_accuracy(trajectories: list[Trajectory]) -> dict:
    """Compute overall accuracy and basic statistics.

    Returns a dict with keys: total, correct, incorrect, no_answer, accuracy.
    """
    total = len(trajectories)
    correct = sum(1 for t in trajectories if t.is_correct)
    no_answer = sum(1 for t in trajectories if t.final_answer is None)
    incorrect = total - correct - no_answer

    return {
        "total": total,
        "correct": correct,
        "incorrect": incorrect,
        "no_answer": no_answer,
        "accuracy": correct / total if total > 0 else 0.0,
    }


def per_category_breakdown(
    trajectories: list[Trajectory],
    category_key: str = "domain",
) -> dict[str, dict]:
    """Compute accuracy broken down by a metadata category.

    Each trajectory must have ``metadata[category_key]`` set.

    Returns:
        Dict mapping category values to accuracy dicts.
    """
    buckets: dict[str, list[Trajectory]] = defaultdict(list)
    for t in trajectories:
        cat = t.metadata.get(category_key, "unknown")
        buckets[cat].append(t)

    results = {}
    for cat, trajs in sorted(buckets.items()):
        results[cat] = compute_accuracy(trajs)
    return results


# ---------------------------------------------------------------------------
# Step-level stats
# ---------------------------------------------------------------------------

def step_level_stats(trajectories: list[Trajectory]) -> dict:
    """Compute aggregate step-level statistics.

    Returns dict with average steps, step-type distribution, etc.
    """
    if not trajectories:
        return {}

    n = len(trajectories)
    total_steps = sum(len(t.steps) for t in trajectories)
    type_counts: dict[str, int] = defaultdict(int)
    for t in trajectories:
        for s in t.steps:
            type_counts[s.step_type] += 1

    # Critique accuracy (if critique steps exist)
    critique_steps = [
        s for t in trajectories for s in t.steps
        if s.step_type == "critique" and s.critique_result is not None
    ]
    critique_correct = sum(1 for s in critique_steps if s.critique_result.is_correct)

    return {
        "avg_total_steps": round(total_steps / n, 2),
        "step_type_distribution": dict(type_counts),
        "total_critique_steps": len(critique_steps),
        "critique_steps_marked_correct": critique_correct,
        "critique_steps_marked_incorrect": len(critique_steps) - critique_correct,
    }


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def generate_report(
    trajectories: list[Trajectory],
    output_path: Optional[str | Path] = None,
) -> dict:
    """Generate a full evaluation report.

    Args:
        trajectories: List of evaluated trajectories.
        output_path: If provided, write the report as JSON to this path.

    Returns:
        The report dict.
    """
    report = {
        "overall": compute_accuracy(trajectories),
        "by_domain": per_category_breakdown(trajectories, "domain"),
        "by_difficulty": per_category_breakdown(trajectories, "difficulty"),
        "step_stats": step_level_stats(trajectories),
    }

    if output_path:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        logger.info("Report written to %s", path)

    return report


def print_report(report: dict) -> None:
    """Pretty-print an evaluation report to stdout."""
    overall = report["overall"]
    print(f"\n{'='*60}")
    print(f"  Overall Accuracy: {overall['correct']}/{overall['total']} "
          f"= {overall['accuracy']:.1%}")
    print(f"  No answer: {overall['no_answer']}")
    print(f"{'='*60}")

    if report.get("by_domain"):
        print("\n  Per-domain breakdown:")
        for domain, stats in report["by_domain"].items():
            print(f"    {domain:30s}  {stats['correct']}/{stats['total']} "
                  f"= {stats['accuracy']:.1%}")

    if report.get("by_difficulty"):
        print("\n  Per-difficulty breakdown:")
        for diff, stats in report["by_difficulty"].items():
            print(f"    {diff:30s}  {stats['correct']}/{stats['total']} "
                  f"= {stats['accuracy']:.1%}")

    step_stats = report.get("step_stats", {})
    if step_stats:
        print(f"\n  Avg steps per problem: {step_stats.get('avg_total_steps', 'N/A')}")
        dist = step_stats.get("step_type_distribution", {})
        if dist:
            print("  Step type distribution:")
            for stype, count in sorted(dist.items()):
                print(f"    {stype:20s}  {count}")

    print()
