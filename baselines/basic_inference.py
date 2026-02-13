#!/usr/bin/env python3
"""Basic inference against a locally-served model using the OpenAI client.

No tools are provided — this is a plain chat completion to see how the model
responds to a math problem on its own.

Usage:
    python baselines/basic_inference.py \
        --problem "What is 2+2?" \
        --model "Qwen/Qwen2.5-Math-7B-Instruct" \
        --temperature 0.0 \
        --top-p 1.0 \
        --max-tokens 2048 \
        --api-base "http://localhost:8000/v1"
"""

from __future__ import annotations

import argparse

from openai import OpenAI


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run basic inference against a locally-served model."
    )
    parser.add_argument(
        "--problem",
        type=str,
        default=None,
        help="Problem text. If not provided, prompts interactively.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="Qwen/Qwen2.5-Math-7B-Instruct",
        help="Model name as served by vLLM (default: Qwen/Qwen2.5-Math-7B-Instruct).",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="Sampling temperature (default: 0.0 for greedy).",
    )
    parser.add_argument(
        "--top-p",
        type=float,
        default=1.0,
        help="Nucleus sampling top-p (default: 1.0).",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=2048,
        help="Maximum number of tokens to generate (default: 2048).",
    )
    parser.add_argument(
        "--api-base",
        type=str,
        default="http://localhost:8000/v1",
        help="Base URL for the vLLM OpenAI-compatible API (default: http://localhost:8000/v1).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # Get problem text
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

    # Create OpenAI client pointing at the local vLLM server
    client = OpenAI(
        base_url=args.api_base,
        api_key="EMPTY",
    )

    print(f"\n{'='*60}")
    print(f"Model:       {args.model}")
    print(f"Temperature: {args.temperature}")
    print(f"Top-p:       {args.top_p}")
    print(f"Max tokens:  {args.max_tokens}")
    print(f"API base:    {args.api_base}")
    print(f"{'='*60}")
    print(f"Problem: {problem}")
    print(f"{'='*60}\n")

    response = client.chat.completions.create(
        model=args.model,
        messages=[
            {"role": "user", "content": problem},
        ],
        temperature=args.temperature,
        top_p=args.top_p,
        max_tokens=args.max_tokens,
    )

    # Display the response
    choice = response.choices[0]
    print("RESPONSE")
    print(f"{'='*60}")
    print(choice.message.content)
    print(f"{'='*60}")
    print(f"Finish reason: {choice.finish_reason}")
    print(f"Usage: prompt={response.usage.prompt_tokens}, "
          f"completion={response.usage.completion_tokens}, "
          f"total={response.usage.total_tokens}")


if __name__ == "__main__":
    main()
