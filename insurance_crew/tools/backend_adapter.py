"""Thin adapter layer for CrewAI to interact with existing backend services.

This module does not implement business logic. It only provides a structured
bridge to the existing services so CrewAI can orchestrate them.
"""

from typing import Any

from database.crud.claim import get_claim
from cv.services.detection_service import DetectionService
from nlp.services.nlp_service import NLPService
from rag.services.rag_service import RAGService
from services.decision_service import DecisionService


class BackendAdapter:
    """Adapter for reusing the existing backend services from CrewAI."""

    def __init__(self) -> None:
        self.detection_service = DetectionService()
        self.nlp_service = NLPService()
        self.rag_service = RAGService()
        self.decision_service = DecisionService()

    def _validate_claim(self, db: Any, claim_id: str) -> None:
        claim = get_claim(db, claim_id)
        if claim is None:
            raise Exception("Claim not found.")

    def run_detection(self, claim_id: str, db: Any = None) -> Any:
        if db is None:
            raise ValueError("A database session is required for the detection workflow.")

        self._validate_claim(db, claim_id)
        predictions = self.detection_service.detect_claim(claim_id)
        return self.detection_service.save_results(db, claim_id, predictions)

    def run_nlp(self, claim_id: str, db: Any = None) -> Any:
        if db is None:
            raise ValueError("A database session is required for the NLP workflow.")

        self._validate_claim(db, claim_id)
        return self.nlp_service.analyze_claim(db, claim_id)

    def run_rag(self, claim_id: str, db: Any = None) -> Any:
        if db is None:
            raise ValueError("A database session is required for the RAG workflow.")

        self._validate_claim(db, claim_id)
        return self.rag_service.verify_policy(db, claim_id)

    def run_decision(self, claim_id: str, db: Any = None) -> Any:
        if db is None:
            raise ValueError("A database session is required for the decision workflow.")

        self._validate_claim(db, claim_id)
        return self.decision_service.process_claim(db, claim_id)
