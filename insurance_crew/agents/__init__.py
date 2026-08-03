"""CrewAI agent package for the insurance claim workflow."""

from __future__ import annotations

from typing import Any

__all__ = ["InsuranceClaimCrew"]


def __getattr__(name: str) -> Any:
    if name == "InsuranceClaimCrew":
        from .crew import InsuranceClaimCrew

        return InsuranceClaimCrew
    raise AttributeError(name)
