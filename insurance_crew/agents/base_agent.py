"""
YAML-backed factory for creating CrewAI Agent objects.
Uses Ollama (Qwen) as the LLM for every agent.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional

import yaml

from crewai import LLM
from crewai.agent.core import Agent


class CrewAgentFactory:
    """Build CrewAI Agent objects from YAML configuration."""

    def __init__(
        self,
        config_path: Optional[str] = None,
    ):

        self.config_path = (
            config_path
            or self._default_config_path()
        )

        self._config = self._load_config()

        # ----------------------------------------
        # Ollama LLM
        # ----------------------------------------

        self.llm = LLM(
            model="ollama/qwen2.5:3b",
            base_url="http://localhost:11434",
            temperature=0,
        )

    def _default_config_path(self) -> str:

        return str(
            Path(__file__).resolve().parents[1]
            / "config"
            / "agents.yaml"
        )

    def _load_config(self) -> Dict[str, Any]:

        with open(
            self.config_path,
            "r",
            encoding="utf-8",
        ) as file:

            payload = yaml.safe_load(file) or {}

        return payload.get(
            "agents",
            {},
        )

    def build(
        self,
        agent_key: str,
        tool: Optional[Any] = None,
    ) -> Agent:

        agent_config = self._config.get(agent_key)

        if not agent_config:

            raise KeyError(
                f"Agent configuration '{agent_key}' not found."
            )

        kwargs = {

            "role": agent_config.get(
                "role",
                "",
            ),

            "goal": agent_config.get(
                "goal",
                "",
            ),

            "backstory": agent_config.get(
                "backstory",
                "",
            ),

            "llm": self.llm,

            "verbose": bool(
                agent_config.get(
                    "verbose",
                    False,
                )
            ),

        }

        # Attach tool only if provided
        if tool is not None:
            kwargs["tools"] = [tool]
        else:
            kwargs["tools"] = []

        return Agent(**kwargs)