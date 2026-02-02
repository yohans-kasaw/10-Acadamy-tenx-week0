"""Tests for the Pydantic models."""
from __future__ import annotations

import pytest

from ..agent_bench.models import InstructionSpec


def test_instruction_spec_valid() -> None:
    data = {"name": "agent-1", "version": 1}
    spec = InstructionSpec.model_validate(data)
    assert spec.name == "agent-1"
    assert spec.version == 1
    assert spec.strict_mode is True


def test_instruction_spec_invalid_name() -> None:
    with pytest.raises(ValueError):
        InstructionSpec.model_validate({"name": "   ", "version": 1})


def test_instruction_spec_extra_fields_forbidden() -> None:
    with pytest.raises(ValueError):
        InstructionSpec.model_validate({"name": "a", "version": 1, "extra": 42})
