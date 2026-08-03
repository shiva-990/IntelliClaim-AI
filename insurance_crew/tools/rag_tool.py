"""CrewAI tool for policy review using the existing RAG pipeline.

This tool delegates to the existing RAGService through the backend adapter.
"""

from __future__ import annotations

from typing import Any, Dict

from .base_tool import BaseTool


class RAGTool(BaseTool):
    """Wrap the existing RAG policy-review flow for CrewAI usage."""

    name: str = "rag_tool"
    description: str = (
        "Runs the existing policy-verification flow for a claim and returns a "
        "structured review result for CrewAI agents."
    )

    def _run(self, claim_id: str, db: Any = None) -> Dict[str, Any]:
        result = self.adapter.run_rag(claim_id, db)
        return {
            "claim_id": claim_id,
            "rag_result": result,
        }
