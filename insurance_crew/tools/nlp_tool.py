"""CrewAI tool for natural-language claim analysis.

This tool delegates to the existing NLPService through the backend adapter.
"""

from __future__ import annotations

from typing import Any, Dict

from .base_tool import BaseTool


class NLPTool(BaseTool):
    """Wrap the existing NLP analysis layer for CrewAI usage."""

    name: str = "nlp_tool"
    description: str = (
        "Runs the existing NLP analysis flow for a claim and returns a "
        "structured result for CrewAI agents."
    )

    def _run(self, claim_id: str, db: Any = None) -> Dict[str, Any]:
        result = self.adapter.run_nlp(claim_id, db)
        return {
            "claim_id": claim_id,
            "nlp_result": self._coerce_to_dict(result),
        }
