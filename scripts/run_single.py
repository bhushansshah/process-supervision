#!/usr/bin/env python3
"""Test the math agent on a single problem (interactive / CLI)."""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import sys
from pathlib import Path

# Ensure the project root is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.agent.math_agent import MathAgent
from src.config import AgentConfig


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the math agent on a single problem.")
    parser.add_argument(
        "--config",
        type=str,
        default="configs/qwen_7b.yaml",
        help="Path to YAML config file.",
    )
    parser.add_argument(
        "--problem",
        type=str,
        default=None,
        help="Problem text. If not provided, prompts interactively.",
    )
    parser.add_argument(
        "--ground-truth",
        type=str,
        default=None,
        help="Optional ground-truth answer for comparison.",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable debug logging.",
    )
    return parser.parse_args()


async def main() -> None:
    args = parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    config = AgentConfig.from_yaml(args.config)

    # Get the problem text
    problem = args.problem
    if problem is None:
        print("Enter your math problem (end with an empty line):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        problem = "\n".join(lines)

    if not problem.strip():
        print("No problem provided. Exiting.")
        return

    print(f"\n{'='*60}")
    print(f"Problem: {problem[:200]}{'...' if len(problem) > 200 else ''}")
    print(f"{'='*60}\n")

    async with MathAgent(config) as agent:
        trajectory = await agent.solve(problem, ground_truth=args.ground_truth)

    # Display results
    print(f"\n{'='*60}")
    print("TRAJECTORY")
    print(f"{'='*60}")
    for step in trajectory.steps:
        print(f"\n[Step {step.step_idx} — {step.step_type}]")
        print(step.content)

    print(f"\n{'='*60}")
    print(f"Final answer: {trajectory.final_answer}")
    if args.ground_truth:
        status = "CORRECT" if trajectory.is_correct else "INCORRECT"
        print(f"Ground truth: {args.ground_truth}")
        print(f"Result: {status}")
    print(f"Total steps: {len(trajectory.steps)}")
    print(f"{'='*60}")

    # Optionally save trajectory
    out_path = Path(config.output_dir) / "single_run.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(trajectory.to_jsonl_dict(), f, indent=2, ensure_ascii=False)
    print(f"\nTrajectory saved to {out_path}")


if __name__ == "__main__":
    asyncio.run(main())
