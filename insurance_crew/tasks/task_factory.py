"""Official CrewAI task factory for the insurance claim workflow."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional

import yaml
from crewai.task import Task

from insurance_crew.agents.base_agent import CrewAgentFactory
from insurance_crew.tools.cv_tool import CVTool
from insurance_crew.tools.nlp_tool import NLPTool
from insurance_crew.tools.rag_tool import RAGTool
from insurance_crew.tools.fraud_tool import FraudTool
from insurance_crew.tools.decision_tool import DecisionTool


class InsuranceTaskFactory:
    """Build official CrewAI Task objects for orchestration only."""

    def __init__(self, config_path: Optional[str] = None) -> None:
        self.config_path = config_path or self._default_config_path()
        self._config = self._load_config()
        self._factory = CrewAgentFactory(str(Path(__file__).resolve().parents[1] / "config" / "agents.yaml"))

    def _default_config_path(self) -> str:
        return str(Path(__file__).resolve().parents[1] / "config" / "tasks.yaml")

    def _load_config(self) -> Dict[str, Any]:
        with open(self.config_path, "r", encoding="utf-8") as handle:
            payload = yaml.safe_load(handle) or {}

        return payload.get("tasks", {})

    def _build_task(self, task_key: str, agent_name: str, description: str, expected_output: str) -> Task:
        task_config = self._config.get(task_key, {})
        tool_map = {
            "vision_agent": CVTool(),
            "claims_agent": NLPTool(),
            "policy_agent": RAGTool(),
            "fraud_agent": FraudTool(),
            "decision_agent": DecisionTool(),
            "report_agent": DecisionTool(),
        }
        agent = self._factory.build(agent_name, tool_map[agent_name])

        return Task(
            description=task_config.get("description", description),
            expected_output=task_config.get("expected_output", expected_output),
            agent=agent,
        )

    def build_vision_task(self) -> Task:
        return self._build_task(
            task_key="vision_task",
            agent_name="vision_agent",
            description="Inspect the claim image evidence and summarize the damage findings.",
            expected_output="A structured summary of damage analysis from the CV tool.",
        )

    def build_claims_task(self) -> Task:
        return self._build_task(
            task_key="claims_task",
            agent_name="claims_agent",
            description="Analyze the claim description and summarize the extracted narrative insights.",
            expected_output="A structured summary of the accident analysis from the NLP tool.",
        )

    def build_policy_task(self) -> Task:
        return self._build_task(
            task_key="policy_task",
            agent_name="policy_agent",
            description="Review policy applicability and summarize coverage findings.",
            expected_output="A structured summary of policy coverage from the RAG tool.",
        )

    def build_fraud_task(self) -> Task:
        return self._build_task(
            task_key="fraud_task",
            agent_name="fraud_agent",
            description="Assess the claim for fraud indicators and summarize the risk findings.",
            expected_output="A structured fraud assessment from the Fraud tool.",
        )

    def build_decision_task(self) -> Task:
        return self._build_task(
            task_key="decision_task",
            agent_name="decision_agent",
            description="Review the prior findings and determine the final claim disposition.",
            expected_output="A final decision of Approve, Reject, or Manual Review.",
        )

    def build_report_task(self) -> Task:
        return self._build_task(
            task_key="report_task",
            agent_name="report_agent",
            description="Compile the final human-readable insurance claim report.",
            expected_output="A polished report summarizing the prior agent findings.",
        )

    def build_all_tasks(self) -> list[Task]:
        return [
            self.build_vision_task(),
            self.build_claims_task(),
            self.build_policy_task(),
            self.build_fraud_task(),
            self.build_decision_task(),
            self.build_report_task(),
        ]
