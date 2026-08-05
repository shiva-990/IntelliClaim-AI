from typing import Any

from database.crud.claim import get_claim

from cv.services.detection_service import DetectionService
from nlp.services.nlp_service import NLPService
from rag.services.rag_service import RAGService
from services.decision_service import DecisionService


# ---------------------------------------------------
# Create service instances ONLY ONCE
# ---------------------------------------------------

_detection_service = DetectionService()
_nlp_service = NLPService()
_rag_service = RAGService()
_decision_service = DecisionService()


class BackendAdapter:

    def __init__(self):

        self.detection_service = _detection_service
        self.nlp_service = _nlp_service
        self.rag_service = _rag_service
        self.decision_service = _decision_service

    def _validate_claim(self, db: Any, claim_id: str):

        claim = get_claim(db, claim_id)

        if claim is None:
            raise Exception("Claim not found.")

    def run_detection(self, claim_id, db):

        self._validate_claim(db, claim_id)

        predictions = self.detection_service.detect_claim(
            claim_id
        )

        return self.detection_service.save_results(
            db,
            claim_id,
            predictions,
        )

    def run_nlp(self, claim_id, db):

        self._validate_claim(db, claim_id)

        return self.nlp_service.analyze_claim(
            db,
            claim_id,
        )

    def run_rag(self, claim_id, db):

        self._validate_claim(db, claim_id)

        return self.rag_service.verify_policy(
            db,
            claim_id,
        )

    def run_decision(self, claim_id, db):

        self._validate_claim(db, claim_id)

        return self.decision_service.process_claim(
            db,
            claim_id,
        )