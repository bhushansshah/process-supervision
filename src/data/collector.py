"""Trajectory collection, serialization, and JSONL export."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Optional

from src.data.trajectory import Trajectory

logger = logging.getLogger(__name__)


class TrajectoryCollector:
    """Collects trajectories during evaluation and writes them to JSONL.

    Usage::

        collector = TrajectoryCollector("results/run_001")
        collector.add(trajectory)
        collector.add(trajectory2)
        collector.flush()  # writes all buffered trajectories to disk
    """

    def __init__(self, output_dir: str | Path, buffer_size: int = 50) -> None:
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.trajectories: list[Trajectory] = []
        self._buffer_size = buffer_size
        self._total_written = 0

    @property
    def output_path(self) -> Path:
        return self.output_dir / "trajectories.jsonl"

    def add(self, trajectory: Trajectory) -> None:
        """Add a trajectory to the buffer. Auto-flushes when buffer is full."""
        self.trajectories.append(trajectory)
        if len(self.trajectories) >= self._buffer_size:
            self.flush()

    def flush(self) -> None:
        """Write all buffered trajectories to the JSONL file."""
        if not self.trajectories:
            return

        with open(self.output_path, "a") as f:
            for traj in self.trajectories:
                line = json.dumps(traj.to_jsonl_dict(), ensure_ascii=False)
                f.write(line + "\n")

        count = len(self.trajectories)
        self._total_written += count
        self.trajectories.clear()
        logger.info(
            "Flushed %d trajectories to %s (total: %d)",
            count,
            self.output_path,
            self._total_written,
        )

    @property
    def total_collected(self) -> int:
        return self._total_written + len(self.trajectories)

    def finalize(self) -> Path:
        """Flush remaining trajectories and return the output path."""
        self.flush()
        logger.info("Collection finalized: %d total trajectories at %s", self._total_written, self.output_path)
        return self.output_path

    @staticmethod
    def load_trajectories(path: str | Path) -> list[Trajectory]:
        """Load trajectories from a JSONL file."""
        trajectories = []
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line:
                    data = json.loads(line)
                    trajectories.append(Trajectory.model_validate(data))
        return trajectories


class SummaryStats:
    """Compute summary statistics from a list of trajectories."""

    def __init__(self, trajectories: list[Trajectory]) -> None:
        self.trajectories = trajectories

    @property
    def total(self) -> int:
        return len(self.trajectories)

    @property
    def correct(self) -> int:
        return sum(1 for t in self.trajectories if t.is_correct)

    @property
    def accuracy(self) -> float:
        return self.correct / self.total if self.total > 0 else 0.0

    @property
    def avg_steps(self) -> float:
        if not self.trajectories:
            return 0.0
        return sum(len(t.steps) for t in self.trajectories) / len(self.trajectories)

    @property
    def avg_reasoning_steps(self) -> float:
        if not self.trajectories:
            return 0.0
        return sum(t.num_reasoning_steps for t in self.trajectories) / len(self.trajectories)

    @property
    def avg_code_steps(self) -> float:
        if not self.trajectories:
            return 0.0
        return sum(t.num_code_steps for t in self.trajectories) / len(self.trajectories)

    def to_dict(self) -> dict:
        return {
            "total": self.total,
            "correct": self.correct,
            "accuracy": self.accuracy,
            "avg_steps": round(self.avg_steps, 2),
            "avg_reasoning_steps": round(self.avg_reasoning_steps, 2),
            "avg_code_steps": round(self.avg_code_steps, 2),
        }
