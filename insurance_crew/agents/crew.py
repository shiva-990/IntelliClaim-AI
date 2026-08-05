"""CrewAI crew definition for the insurance claim workflow.

This module uses CrewAI 1.15 project architecture with real
CrewAI Agent, Task, and Crew objects.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from crewai.agent.core import Agent
from crewai.crew import Crew
from crewai.project import CrewBase, agent, crew, task
from crewai.task import Task

from ..tools.cv_tool import CVTool
from ..tools.nlp_tool import NLPTool
from ..tools.rag_tool import RAGTool
from ..tools.fraud_tool import FraudTool
from ..tools.decision_tool import DecisionTool
from ..tools.report_tool import ReportTool
from .base_agent import CrewAgentFactory


@CrewBase
class InsuranceClaimCrew:
    """Crew for orchestrating insurance claim analysis."""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def __init__(self):

        self.base_directory = Path(__file__).resolve().parents[1]

        self._factory = CrewAgentFactory(
            str(
                self.base_directory
                / "config"
                / "agents.yaml"
            )
        )

    # =====================================================
    # Agents
    # =====================================================

    @agent
    def vision_agent(self) -> Agent:
        return self._factory.build(
            "vision_agent",
            CVTool(),
        )

    @agent
    def claims_agent(self) -> Agent:
        return self._factory.build(
            "claims_agent",
            NLPTool(),
        )

    @agent
    def policy_agent(self) -> Agent:
        return self._factory.build(
            "policy_agent",
            RAGTool(),
        )

    @agent
    def fraud_agent(self) -> Agent:
        return self._factory.build(
            "fraud_agent",
            FraudTool(),
        )

    @agent
    def decision_agent(self) -> Agent:
        return self._factory.build(
            "decision_agent",
            DecisionTool(),
        )

    @agent
    def report_agent(self) -> Agent:
        return self._factory.build(
            "report_agent",
            ReportTool(),
        )

    # =====================================================
    # Tasks
    # =====================================================

    @task
    def vision_task(self) -> Task:
        return Task(
            description=(
                "Inspect the uploaded vehicle image and summarize the detected damage."
            ),
            expected_output=(
                "A structured summary of the computer vision analysis."
            ),
            agent=self.vision_agent(),
        )

    @task
    def claims_task(self) -> Task:
        return Task(
            description=(
                "Analyze the accident description and extract structured accident information."
            ),
            expected_output=(
                "A structured NLP summary."
            ),
            agent=self.claims_agent(),
        )

    @task
    def policy_task(self) -> Task:
        return Task(
            description=(
                "Review the customer's insurance policy and determine coverage."
            ),
            expected_output=(
                "A policy verification summary."
            ),
            agent=self.policy_agent(),
        )

    @task
    def fraud_task(self) -> Task:
        return Task(
            description=(
                "Assess fraud indicators and summarize the findings."
            ),
            expected_output=(
                "A fraud assessment."
            ),
            agent=self.fraud_agent(),
        )

    @task
    def decision_task(self) -> Task:
        return Task(
            description=(
                "Review all previous analyses and determine Approve, Reject or Manual Review."
            ),
            expected_output=(
                "Final claim decision."
            ),
            agent=self.decision_agent(),
        )

    @task
    def report_task(self) -> Task:
        return Task(
            description=(
                "Generate a professional executive summary of the insurance claim."
            ),
            expected_output=(
                "A final human-readable insurance claim report."
            ),
            agent=self.report_agent(),
        )

    # =====================================================
    # Crew
    # =====================================================

    @crew
    def crew(self) -> Crew:

        return Crew(

            agents=[

                self.vision_agent(),

                self.claims_agent(),

                self.policy_agent(),

                self.fraud_agent(),

                self.decision_agent(),

                self.report_agent(),

            ],

            tasks=[

                self.vision_task(),

                self.claims_task(),

                self.policy_task(),

                self.fraud_task(),

                self.decision_task(),

                self.report_task(),

            ],

            process="sequential",

            verbose=True,

        )

    # =====================================================
    # Public API
    # =====================================================

    def kickoff(
        self,
        claim_id: str,
        db: Any = None,
    ):

        return self.crew().kickoff(
            inputs={
                "claim_id": claim_id,
                "db": db,
            }
        )