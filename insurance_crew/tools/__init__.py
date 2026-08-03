"""CrewAI tools package.

These tools are intentionally thin wrappers around the backend adapter so
CrewAI can orchestrate existing services without implementing business logic.
"""

from .backend_adapter import BackendAdapter
from .base_tool import BaseTool
from .cv_tool import CVTool
from .nlp_tool import NLPTool
from .rag_tool import RAGTool
from .fraud_tool import FraudTool
from .decision_tool import DecisionTool

__all__ = [
    "BackendAdapter",
    "BaseTool",
    "CVTool",
    "NLPTool",
    "RAGTool",
    "FraudTool",
    "DecisionTool",
]
