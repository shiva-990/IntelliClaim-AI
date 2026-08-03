"""CrewAI tool for final decision synthesis.

This tool delegates to the existing DecisionService through the backend
adapter and returns a clean, structured outcome for CrewAI agents.
"""

from __future__ import annotations

from typing import Any, Dict

from .base_tool import BaseTool


class DecisionTool(BaseTool):
    """Wrap the existing decision engine for CrewAI usage."""

    name: str = "decision_tool"
    description: str = (
        "Runs the existing decision engine for a claim and returns a compact "
        "decision payload for CrewAI agents."
    )

    def _run(self, claim_id: str, db: Any = None) -> Dict[str, Any]:
        result = self.adapter.run_decision(claim_id, db)
        data = self._coerce_to_dict(result)

        return {
            "claim_id": claim_id,
            "coverage": data.get("coverage"),
            "fraud_score": data.get("fraud_score"),
            "decision": data.get("decision"),
            "reason": data.get("reason"),
        }
