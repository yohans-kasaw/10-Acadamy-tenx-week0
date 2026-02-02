"""Pydantic models for instruction specs.

Google-style docstrings are used and all fields are typed.
"""
from pydantic import BaseModel, ConfigDict, field_validator


class InstructionSpec(BaseModel):
    """Specification for an instruction or benchmark target.

    Attributes:
        name: The unique name for the instruction set.
        version: Integer version number.
        strict_mode: Whether to apply strict evaluation rules.
    """

    model_config = ConfigDict(extra="forbid")

    name: str
    version: int
    strict_mode: bool = True

    @field_validator("name")
    @classmethod
    def name_not_empty(cls, v: str) -> str:
        """Validate that the name is not empty."""
        if not v.strip():
            raise ValueError("name must not be empty")
        return v
