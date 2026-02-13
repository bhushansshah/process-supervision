#!/usr/bin/env python3
"""Batch evaluation on the Omni-MATH dataset."""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import sys
import time
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.agent.math_agent import MathAgent
from src.config import AgentConfig
from src.data.collector import TrajectoryCollector
from src.data.trajectory import Trajectory
from src.evaluation.answer_extraction import compare_answers, extract_boxed_answer
from src.evaluation.metrics import generate_report, print_report
from src.evaluation.omnimath import MathProblem, load_omnimath


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Evaluate math agent on Omni-MATH.")
    p.add_argument("--config", type=str, default="configs/qwen_7b.yaml")
    p.add_argument("--domain", type=str, default=None, help="Filter by domain.")
    p.add_argument("--difficulty", type=str, default=None, help="Filter by difficulty.")
    p.add_argument("--max-problems", type=int, default=None, help="Max problems to evaluate.")
    p.add_argument("--concurrency", type=int, default=1, help="Number of concurrent solves.")
    p.add_argument("--output-dir", type=str, default=None, help="Override output directory.")
    p.add_argument("--verbose", "-v", action="store_true")
    return p.parse_args()


async def solve_one(
    agent: MathAgent,
    problem: MathProblem,
    semaphore: asyncio.Semaphore,
) -> Trajectory:
    """Solve a single problem with concurrency control."""
    async with semaphore:
        logging.info("Solving problem %d: %s...", problem.idx, problem.question[:80])
        trajectory = await agent.solve(
            problem=problem.question,
            ground_truth=problem.answer,
        )
        # Attach metadata for per-category breakdowns
        trajectory.metadata["domain"] = problem.domain
        trajectory.metadata["difficulty"] = problem.difficulty
        trajectory.metadata["problem_idx"] = problem.idx

        # Re-evaluate correctness with the robust comparison
        if trajectory.final_answer and problem.answer:
            trajectory.is_correct = compare_answers(
                trajectory.final_answer, problem.answer
            )

        return trajectory


async def main() -> None:
    args = parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    config = AgentConfig.from_yaml(args.config)
    if args.output_dir:
        config.output_dir = args.output_dir

    # Load dataset
    problems = load_omnimath(
        domain=args.domain,
        difficulty=args.difficulty,
        max_problems=args.max_problems,
    )
    if not problems:
        print("No problems matched the filters. Exiting.")
        return

    print(f"Evaluating on {len(problems)} problems (concurrency={args.concurrency})")

    collector = TrajectoryCollector(config.output_dir)
    semaphore = asyncio.Semaphore(args.concurrency)

    start_time = time.time()

    async with MathAgent(config) as agent:
        tasks = [solve_one(agent, p, semaphore) for p in problems]
        trajectories: list[Trajectory] = []

        for coro in asyncio.as_completed(tasks):
            traj = await coro
            trajectories.append(traj)
            collector.add(traj)

            # Progress
            done = len(trajectories)
            correct_so_far = sum(1 for t in trajectories if t.is_correct)
            elapsed = time.time() - start_time
            print(
                f"  [{done}/{len(problems)}] "
                f"acc={correct_so_far}/{done} "
                f"({correct_so_far/done:.1%}) "
                f"elapsed={elapsed:.1f}s"
            )

    collector.finalize()
    elapsed_total = time.time() - start_time

    # Generate and print report
    report_path = Path(config.output_dir) / "report.json"
    report = generate_report(trajectories, output_path=report_path)
    print_report(report)

    print(f"Total time: {elapsed_total:.1f}s ({elapsed_total/len(problems):.1f}s per problem)")
    print(f"Trajectories: {collector.output_path}")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    asyncio.run(main())
