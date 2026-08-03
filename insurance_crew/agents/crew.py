"""CrewAI crew definition for the insurance claim workflow.

This module now uses the installed CrewAI 1.15 project architecture with real
CrewAI Agent, Task, and Crew objects. It keeps the existing tools and
backend adapter as the integration boundary.
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
from .base_agent import CrewAgentFactory


@CrewBase
class InsuranceClaimCrew:
    """Crew for orchestrating insurance-claim analysis with CrewAI 1.15."""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def __init__(self) -> None:
        self.base_directory = Path(__file__).resolve().parents[1]
        self._factory = CrewAgentFactory(str(self.base_directory / "config" / "agents.yaml"))

    @agent
    def vision_agent(self) -> Agent:
        return self._factory.build("vision_agent", CVTool())

    @agent
    def claims_agent(self) -> Agent:
        return self._factory.build("claims_agent", NLPTool())

    @agent
    def policy_agent(self) -> Agent:
        return self._factory.build("policy_agent", RAGTool())

    @agent
    def fraud_agent(self) -> Agent:
        return self._factory.build("fraud_agent", FraudTool())

    @agent
    def decision_agent(self) -> Agent:
        return self._factory.build("decision_agent", DecisionTool())

    @agent
    def report_agent(self) -> Agent:
        return self._factory.build("report_agent", DecisionTool())

    @task
    def vision_task(self) -> Task:
        return Task(
            description="Inspect the claim image evidence and summarize the damage findings.",
            expected_output="A structured summary of damage analysis from the CV tool.",
            agent=self.vision_agent(),
        )

    @task
    def claims_task(self) -> Task:
        return Task(
            description="Analyze the claim description and summarize the extracted narrative insights.",
            expected_output="A structured summary of the accident analysis from the NLP tool.",
            agent=self.claims_agent(),
        )

    @task
    def policy_task(self) -> Task:
        return Task(
            description="Review policy applicability and summarize coverage findings.",
            expected_output="A structured summary of policy coverage from the RAG tool.",
            agent=self.policy_agent(),
        )

    @task
    def fraud_task(self) -> Task:
        return Task(
            description="Assess the claim for fraud indicators and summarize the risk findings.",
            expected_output="A structured fraud assessment from the Fraud tool.",
            agent=self.fraud_agent(),
        )

    @task
    def decision_task(self) -> Task:
        return Task(
            description="Review the prior findings and determine the final claim disposition.",
            expected_output="A final decision of Approve, Reject, or Manual Review.",
            agent=self.decision_agent(),
        )

    @task
    def report_task(self) -> Task:
        return Task(
            description="Compile the final human-readable insurance claim report.",
            expected_output="A polished report summarizing the prior agent findings.",
            agent=self.report_agent(),
        )

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

    def kickoff(self, claim_id: str, db: Any = None) -> Any:
        """Public entry point for orchestrating the insurance claim workflow."""
        return self.crew().kickoff(inputs={"claim_id": claim_id, "db": db})
