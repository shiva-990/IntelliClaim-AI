"""Base abstractions for CrewAI tools in this project.

These tool classes are intentionally thin wrappers around the existing backend
adapter so CrewAI can orchestrate behavior without reimplementing business
logic.
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from crewai.tools.base_tool import BaseTool as CrewBaseTool

from .backend_adapter import BackendAdapter


class BaseTool(CrewBaseTool):
    """Thin adapter around the official CrewAI BaseTool."""

    name: str = "base_tool"
    description: str = "Base tool interface for CrewAI orchestration."
    adapter: Any = None

    def __init__(self, adapter: Optional[BackendAdapter] = None) -> None:
        super().__init__()
        self.adapter = adapter or BackendAdapter()

    def _run(self, claim_id: str, db: Any = None) -> Any:
        raise NotImplementedError

    def run(self, claim_id: str, db: Any = None) -> Any:
        """Public run entry point used by higher-level orchestration."""
        return self._run(claim_id, db)

    @staticmethod
    def _coerce_to_dict(value: Any) -> Dict[str, Any]:
        """Convert backend objects to plain dictionaries for agent consumption."""
        if isinstance(value, dict):
            return value

        if hasattr(value, "__dict__"):
            return {
                key: item
                for key, item in vars(value).items()
                if not key.startswith("_")
            }

        return {"value": value}
