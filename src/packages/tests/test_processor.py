"""Tests for the processor utilities including async benchmark."""
from __future__ import annotations

import pytest

from ..agent_bench.processor import load_spec, run_benchmark


def test_load_spec_valid() -> None:
    data = {"name": "agent-x", "version": 2}
    spec = load_spec(data)
    assert spec.name == "agent-x"


@pytest.mark.asyncio
async def test_run_benchmark_async() -> None:
    data = {"name": "agent-x", "version": 2}
    spec = load_spec(data)

    score = await run_benchmark(spec, iterations=3)
    assert isinstance(score, float)
    # deterministic check
    expected = sum((len(spec.name) + float(spec.version)) / (i + 1) for i in range(3))
    assert score == pytest.approx(expected)
