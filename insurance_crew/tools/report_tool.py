"""
CrewAI Report Tool
"""

from __future__ import annotations

from insurance_crew.tools.base_tool import BaseTool


class ReportTool(BaseTool):
    """
    Report generation tool.
    """

    name: str = "report_tool"

    description: str = (
        "Generate an executive insurance claim report "
        "using the backend analysis results."
    )

    def _run(
        self,
        claim_id: str = "",
        cv_result: str = "",
        nlp_result: str = "",
        rag_result: str = "",
        decision_result: str = "",
        **kwargs,
    ) -> str:

        report = f"""
===============================
 Executive Insurance Report
===============================

Claim ID
--------
{claim_id}

Computer Vision
---------------
{cv_result}

NLP Analysis
------------
{nlp_result}

Policy Verification
-------------------
{rag_result}

Decision
--------
{decision_result}

===============================
End of Report
===============================
"""

        return report