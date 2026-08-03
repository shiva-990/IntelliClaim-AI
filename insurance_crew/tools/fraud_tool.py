"""CrewAI tool for fraud-focused claim assessment.

This tool delegates to the existing decision service through the backend
adapter and extracts the fraud-related portion of the result.
"""

from __future__ import annotations

from typing import Any, Dict

from .base_tool import BaseTool


class FraudTool(BaseTool):
    """Expose fraud-related evaluation from the existing decision flow."""

    name: str = "fraud_tool"
    description: str = (
        "Extracts the fraud-risk signal from the existing decision workflow "
        "for CrewAI agents."
    )

    def _run(self, claim_id: str, db: Any = None) -> Dict[str, Any]:
        result = self.adapter.run_decision(claim_id, db)
        data = self._coerce_to_dict(result)

        return {
            "claim_id": claim_id,
            "fraud_score": data.get("fraud_score"),
            "decision": data.get("decision"),
            "reason": data.get("reason"),
        }
