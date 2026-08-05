"""
CrewAI crew for generating the final executive insurance report.

The backend (CV, NLP, RAG and Decision Engine) has already completed
its work before CrewAI starts.

CrewAI is responsible ONLY for producing the final executive report.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from crewai import Crew, Task
from crewai.project import CrewBase, agent, crew

from insurance_crew.agents.base_agent import CrewAgentFactory


@CrewBase
class InsuranceClaimCrew:

    agents_config = "config/agents.yaml"

    tasks_config = "config/tasks.yaml"

    def __init__(self):

        self.base_directory = Path(__file__).resolve().parents[1]

        self.factory = CrewAgentFactory(

            str(

                self.base_directory

                / "config"

                / "agents.yaml"

            )

        )

    # -------------------------------------------------------
    # Report Agent
    # -------------------------------------------------------

    @agent
    def report_agent(self):

        return self.factory.build("report_agent")

    # -------------------------------------------------------
    # Crew
    # -------------------------------------------------------

    @crew
    def crew(self):

        report_task = Task(

            description="""
You are an expert insurance claims analyst.

The backend has already completed all processing.

Use ONLY the information below.

====================================================

Claim ID

{claim_id}

====================================================

Computer Vision Results

{cv_result}

====================================================

NLP Results

{nlp_result}

====================================================

Policy Verification

{rag_result}

====================================================

Decision Engine

{decision_result}

====================================================

Generate a professional insurance report.

Include the following sections.

1. Executive Summary

2. Damage Assessment

3. Accident Analysis

4. Policy Coverage

5. Fraud Assessment

6. Final Decision

7. Recommendation

Use professional business language.
""",

            expected_output="""
A professional executive insurance claim report.
""",

            agent=self.report_agent(),

        )

        return Crew(

            agents=[

                self.report_agent(),

            ],

            tasks=[

                report_task,

            ],

            process="sequential",

            verbose=True,

        )

    # -------------------------------------------------------
    # Public API
    # -------------------------------------------------------

    def kickoff(

        self,

        claim_id: str,

        cv_result: Any,

        nlp_result: Any,

        rag_result: Any,

        decision_result: Any,

    ):

        return self.crew().kickoff(

            inputs={

                "claim_id": claim_id,

                "cv_result": cv_result,

                "nlp_result": nlp_result,

                "rag_result": rag_result,

                "decision_result": decision_result,

            }

        )