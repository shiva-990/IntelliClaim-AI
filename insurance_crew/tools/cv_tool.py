"""CrewAI tool for computer-vision claim analysis.

This tool delegates to the existing DetectionService through the backend
adapter without duplicating any backend behavior.
"""

from __future__ import annotations

from typing import Any, Dict

from .base_tool import BaseTool


class CVTool(BaseTool):
    """Wrap the existing CV detection layer for CrewAI usage."""

    name: str = "cv_tool"
    description: str = (
        "Runs the existing computer-vision detection flow for a claim and "
        "returns a structured result for CrewAI agents."
    )

    def _run(self, claim_id: str, db: Any = None) -> Dict[str, Any]:
        result = self.adapter.run_detection(claim_id, db)
        return {
            "claim_id": claim_id,
            "cv_result": result,
        }
