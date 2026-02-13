#!/usr/bin/env python3
"""Error analysis: categorize failures and identify where the agent went wrong.

Failure categories:
  - no_answer:          Agent exhausted max turns without producing \\boxed{}
  - wrong_reasoning:    Final answer wrong, no code was used
  - computation_error:  Code execution returned an error / traceback
  - critique_missed:    Critique marked a wrong step as correct
  - critique_rejected:  Critique flagged an error but the model didn't fix it
  - wrong_code_logic:   Code ran successfully but produced wrong result
  - other:              Doesn't fit neatly into the above buckets
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.data.collector import TrajectoryCollector
from src.data.trajectory import StepType, Trajectory


# ---------------------------------------------------------------------------
# Failure classification
# ---------------------------------------------------------------------------

def classify_failure(traj: Trajectory) -> str:
    """Classify a single incorrect trajectory into a failure category."""
    if traj.is_correct:
        return "correct"  # not a failure

    if traj.final_answer is None:
        return "no_answer"

    has_code = any(s.step_type == StepType.CODE.value for s in traj.steps)
    has_code_error = any(
        s.step_type == StepType.CODE_OUTPUT.value and "Error" in s.content
        for s in traj.steps
    )
    has_critique = any(s.step_type == StepType.CRITIQUE.value for s in traj.steps)

    # Check if code produced an error
    if has_code_error:
        return "computation_error"

    # Check critique-related failures
    if has_critique:
        critique_steps = [
            s for s in traj.steps
            if s.step_type == StepType.CRITIQUE.value and s.critique_result is not None
        ]
        # Critique said everything was correct but the final answer is wrong
        all_correct = all(s.critique_result.is_correct for s in critique_steps)
        if all_correct and critique_steps:
            return "critique_missed"

        # Critique found errors but the model still got it wrong
        any_flagged = any(not s.critique_result.is_correct for s in critique_steps)
        if any_flagged:
            return "critique_rejected"

    # Code ran but answer is wrong (logic error in the code)
    if has_code and not has_code_error:
        return "wrong_code_logic"

    # Pure reasoning failure (no code used)
    if not has_code:
        return "wrong_reasoning"

    return "other"


# ---------------------------------------------------------------------------
# Analysis report
# ---------------------------------------------------------------------------

def analyze(trajectories: list[Trajectory]) -> dict:
    """Produce a full error analysis report."""
    total = len(trajectories)
    correct = [t for t in trajectories if t.is_correct]
    incorrect = [t for t in trajectories if not t.is_correct]

    # Classify each failure
    failure_categories: Counter = Counter()
    categorized: dict[str, list[Trajectory]] = defaultdict(list)
    for t in incorrect:
        cat = classify_failure(t)
        failure_categories[cat] += 1
        categorized[cat].append(t)

    # Per-category examples (first problem of each)
    examples: dict[str, dict] = {}
    for cat, trajs in categorized.items():
        t = trajs[0]
        examples[cat] = {
            "problem": t.problem[:200],
            "final_answer": t.final_answer,
            "ground_truth": t.ground_truth,
            "num_steps": len(t.steps),
        }

    # Step statistics for correct vs incorrect
    correct_avg_steps = (
        sum(len(t.steps) for t in correct) / len(correct) if correct else 0
    )
    incorrect_avg_steps = (
        sum(len(t.steps) for t in incorrect) / len(incorrect) if incorrect else 0
    )

    # Code usage rates
    correct_code_rate = (
        sum(1 for t in correct if any(s.step_type == StepType.CODE.value for s in t.steps))
        / len(correct) if correct else 0
    )
    incorrect_code_rate = (
        sum(1 for t in incorrect if any(s.step_type == StepType.CODE.value for s in t.steps))
        / len(incorrect) if incorrect else 0
    )

    return {
        "summary": {
            "total": total,
            "correct": len(correct),
            "incorrect": len(incorrect),
            "accuracy": len(correct) / total if total else 0,
        },
        "failure_categories": dict(failure_categories.most_common()),
        "failure_rate_by_category": {
            cat: count / len(incorrect) if incorrect else 0
            for cat, count in failure_categories.most_common()
        },
        "examples": examples,
        "step_comparison": {
            "correct_avg_steps": round(correct_avg_steps, 2),
            "incorrect_avg_steps": round(incorrect_avg_steps, 2),
        },
        "code_usage": {
            "correct_code_rate": round(correct_code_rate, 3),
            "incorrect_code_rate": round(incorrect_code_rate, 3),
        },
    }


def print_analysis(report: dict) -> None:
    """Pretty-print the error analysis."""
    summary = report["summary"]
    print(f"\n{'='*60}")
    print("  ERROR ANALYSIS REPORT")
    print(f"{'='*60}")
    print(f"  Total: {summary['total']}  |  "
          f"Correct: {summary['correct']}  |  "
          f"Incorrect: {summary['incorrect']}  |  "
          f"Accuracy: {summary['accuracy']:.1%}")

    print(f"\n  Failure categories:")
    for cat, count in report["failure_categories"].items():
        rate = report["failure_rate_by_category"][cat]
        print(f"    {cat:25s}  {count:4d}  ({rate:.1%} of failures)")

    print(f"\n  Step comparison:")
    sc = report["step_comparison"]
    print(f"    Correct trajectories avg steps:   {sc['correct_avg_steps']}")
    print(f"    Incorrect trajectories avg steps:  {sc['incorrect_avg_steps']}")

    cu = report["code_usage"]
    print(f"\n  Code usage:")
    print(f"    Correct trajectories with code:    {cu['correct_code_rate']:.1%}")
    print(f"    Incorrect trajectories with code:  {cu['incorrect_code_rate']:.1%}")

    print(f"\n  Example failures:")
    for cat, ex in report["examples"].items():
        print(f"\n    [{cat}]")
        print(f"      Problem:      {ex['problem']}")
        print(f"      Predicted:    {ex['final_answer']}")
        print(f"      Ground truth: {ex['ground_truth']}")
        print(f"      Steps:        {ex['num_steps']}")

    print(f"\n{'='*60}\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Analyze evaluation results.")
    p.add_argument(
        "trajectories_path",
        type=str,
        help="Path to trajectories JSONL file.",
    )
    p.add_argument(
        "--output", "-o",
        type=str,
        default=None,
        help="Path to write the analysis report JSON.",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()

    trajectories = TrajectoryCollector.load_trajectories(args.trajectories_path)
    print(f"Loaded {len(trajectories)} trajectories from {args.trajectories_path}")

    report = analyze(trajectories)
    print_analysis(report)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"Report saved to {out_path}")


if __name__ == "__main__":
    main()
