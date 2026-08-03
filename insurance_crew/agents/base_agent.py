"""YAML-backed factory for creating real CrewAI Agent objects.

This module no longer defines a custom agent framework. It simply loads the
existing YAML configuration and builds real CrewAI Agent instances for the
crew orchestration layer.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional

import yaml
from crewai.agent.core import Agent


class CrewAgentFactory:
    """Build real CrewAI Agent objects from the YAML configuration."""

    def __init__(self, config_path: Optional[str] = None) -> None:
        self.config_path = config_path or self._default_config_path()
        self._config = self._load_config()

    def _default_config_path(self) -> str:
        return str(Path(__file__).resolve().parents[1] / "config" / "agents.yaml")

    def _load_config(self) -> Dict[str, Any]:
        with open(self.config_path, "r", encoding="utf-8") as handle:
            payload = yaml.safe_load(handle) or {}

        return payload.get("agents", {})

    def build(self, agent_key: str, tool: Any) -> Agent:
        """Create a real CrewAI Agent object from YAML configuration."""
        agent_config = self._config.get(agent_key)
        if not agent_config:
            raise KeyError(f"Agent configuration '{agent_key}' was not found.")

        return Agent(
            role=agent_config.get("role", ""),
            goal=agent_config.get("goal", ""),
            backstory=agent_config.get("backstory", ""),
            tools=[tool],
            verbose=bool(agent_config.get("verbose", False)),
        )
