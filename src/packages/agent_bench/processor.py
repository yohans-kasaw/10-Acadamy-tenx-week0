"""Processing utilities for benchmarks and instruction validation."""
from __future__ import annotations

import asyncio
from typing import Dict

from .models import InstructionSpec


def load_spec(data: Dict[str, object]) -> InstructionSpec:
    """Validate and construct an InstructionSpec from raw data.

    Args:
        data: Raw input mapping.

    Returns:
        A validated InstructionSpec instance.
    """
    return InstructionSpec.model_validate(data)


async def run_benchmark(spec: InstructionSpec, iterations: int = 10) -> float:
    """Run a simple asynchronous benchmark and return a score.

    The benchmark is synthetic and deterministic to make testing easy.

    Args:
        spec: The validated instruction spec to benchmark.
        iterations: Number of iterations to simulate.

    Returns:
        A float score representing the benchmark result.
    """
    total: float = 0.0
    for i in range(max(1, iterations)):
        # Yield control to the event loop to simulate async work.
        await asyncio.sleep(0)
        total += (len(spec.name) + float(spec.version)) / (i + 1)
    return total
