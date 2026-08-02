from database.crud.claim import get_claim

from cv.services.detection_service import DetectionService
from nlp.services.nlp_service import NLPService
from rag.services.rag_service import RAGService
from services.decision_service import DecisionService


class ClaimProcessingService:

    def __init__(self):

        self.cv = DetectionService()

        self.nlp = NLPService()

        self.rag = RAGService()

        self.decision = DecisionService()

    def process_claim(
        self,
        db,
        claim_id: str,
    ):

        # --------------------------
        # Check Claim
        # --------------------------
        claim = get_claim(
            db,
            claim_id,
        )

        if claim is None:
            raise Exception(
                "Claim not found."
            )

        # --------------------------
        # CV Module
        # --------------------------
        predictions = self.cv.detect_claim(
            claim_id
        )

        cv_result = self.cv.save_results(
            db,
            claim_id,
            predictions,
        )

        # --------------------------
        # NLP Module
        # --------------------------
        nlp_result = self.nlp.analyze_claim(
            db,
            claim_id,
        )

        # --------------------------
        # RAG Module
        # --------------------------
        rag_result = self.rag.verify_policy(
            db,
            claim_id,
        )

        # --------------------------
        # Decision Engine
        # --------------------------
        decision = self.decision.process_claim(
            db,
            claim_id,
        )

        # --------------------------
        # Final Response
        # --------------------------
        return {

            "claim_id": claim_id,

            "cv": {
                "images_processed": len(predictions),
                "status": "Completed",
            },

            "nlp": {
                "status": "Completed",
                "analysis": {
                    "accident_type": nlp_result.accident_type,
                    "vehicle_part": nlp_result.vehicle_part,
                    "weather": nlp_result.weather,
                    "severity": nlp_result.severity,
                    "cause": nlp_result.cause,
                },
            },

            "rag": {
                "status": "Completed",
                "response": rag_result,
            },

            "decision": {
                "coverage": decision.coverage,
                "fraud_score": decision.fraud_score,
                "decision": decision.decision,
                "reason": decision.reason,
            },
        }