from database.crud.claim import get_claim
import json

from cv.services.detection_service import DetectionService
from nlp.services.nlp_service import NLPService
from rag.services.rag_service import RAGService
from services.decision_service import DecisionService

from insurance_crew.crew import InsuranceClaimCrew


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

        # ---------------------------------------
        # Validate Claim
        # ---------------------------------------

        claim = get_claim(
            db,
            claim_id,
        )

        if claim is None:
            raise Exception(
                "Claim not found."
            )

        # ---------------------------------------
        # Computer Vision
        # ---------------------------------------

        predictions = self.cv.detect_claim(
            claim_id
        )

        cv_result = self.cv.save_results(
            db,
            claim_id,
            predictions,
        )

        # ---------------------------------------
        # NLP
        # ---------------------------------------

        nlp_result = self.nlp.analyze_claim(
            db,
            claim_id,
        )

        # ---------------------------------------
        # RAG
        # ---------------------------------------

        rag_result = self.rag.verify_policy(
            db,
            claim_id,
        )

        # ---------------------------------------
        # Decision
        # ---------------------------------------

        decision = self.decision.process_claim(
            db,
            claim_id,
        )

        # ==========================================================
        # Convert SQLAlchemy objects into dictionaries
        # ==========================================================

        cv_data = []

        for item in cv_result:

            cv_data.append({

                "image_name": item.image_name,

                "severity": item.severity,

                "repair_cost": item.repair_cost,

                "repair_days": item.repair_days,

                "repairable": item.repairable,

                "detections": item.detections,

            })

        nlp_data = {

            "accident_type": nlp_result.accident_type,

            "vehicle_part": nlp_result.vehicle_part,

            "weather": nlp_result.weather,

            "severity": nlp_result.severity,

            "cause": nlp_result.cause,

        }

        decision_data = {

            "coverage": decision.coverage,

            "fraud_score": decision.fraud_score,

            "decision": decision.decision,

            "reason": decision.reason,

        }

        # ==========================================================
        # CrewAI Executive Report
        # ==========================================================

        crew = InsuranceClaimCrew()

        crew_report = crew.kickoff(
            claim_id=claim_id,
            cv_result=json.dumps(cv_data, indent=2),
            nlp_result=json.dumps(nlp_data, indent=2),
            rag_result=str(rag_result),
            decision_result=json.dumps(decision_data, indent=2),
        )

        # ==========================================================
        # Final Response
        # ==========================================================

        return {

            "claim_id": claim_id,

            "cv": {

                "status": "Completed",

                "images_processed": len(predictions),

                "results": cv_data,

            },

            "nlp": {

                "status": "Completed",

                "analysis": nlp_data,

            },

            "rag": {

                "status": "Completed",

                "response": rag_result,

            },

            "decision": decision_data,

            "crew_report": str(crew_report),

        }