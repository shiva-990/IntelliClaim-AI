"""
Base Tool for all CrewAI tools.

Each tool receives structured backend results (CV, NLP, RAG,
Decision) from ClaimProcessingService.

No backend service is called from the tool.
"""

from __future__ import annotations

from typing import Any, Dict

from crewai.tools import BaseTool as CrewBaseTool


class BaseTool(CrewBaseTool):
    """Base class for all CrewAI tools."""

    name: str = "base_tool"

    description: str = "Base Tool"

    def _run(self, **kwargs) -> Any:
        """
        Must be implemented by child classes.
        """
        raise NotImplementedError(
            "Tool must implement _run()."
        )

    def run(self, **kwargs) -> Any:
        """
        CrewAI entry point.

        Accepts any keyword arguments passed by the Crew.
        """
        return self._run(**kwargs)

    @staticmethod
    def to_dict(value: Any):

        """
        Convert SQLAlchemy/Pydantic objects into plain Python
        dictionaries for CrewAI consumption.
        """

        if value is None:
            return None

        if isinstance(value, dict):
            return value

        if isinstance(value, list):

            converted = []

            for item in value:
                converted.append(
                    BaseTool.to_dict(item)
                )

            return converted

        if hasattr(value, "model_dump"):
            return value.model_dump()

        if hasattr(value, "__dict__"):

            data = {}

            for key, val in vars(value).items():

                if key.startswith("_"):
                    continue

                data[key] = BaseTool.to_dict(val)

            return data

        return value