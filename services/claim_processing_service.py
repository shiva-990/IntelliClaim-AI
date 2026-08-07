from database.crud.claim import get_claim

from configs.settings import settings

from cv.services.detection_service import DetectionService
from nlp.services.nlp_service import NLPService
from rag.services.rag_service import RAGService
from services.decision_service import DecisionService
from insurance_crew.crew import InsuranceClaimCrew


class ClaimProcessingService:

    def __init__(self):

        if not settings.DEMO_MODE:
            self.cv = DetectionService()
            self.nlp = NLPService()
            self.rag = RAGService()
            self.decision = DecisionService()

    def process_claim(
        self,
        db,
        claim_id: str,
    ):

        claim = get_claim(db, claim_id)

        if claim is None:
            raise Exception("Claim not found.")

        # ==========================================================
        # DEMO MODE (Railway)
        # ==========================================================
        if settings.DEMO_MODE:

            cv_data = [
                {
                    "image_name": "vehicle.jpg",
                    "severity": "Medium",
                    "repair_cost": 25000,
                    "repair_days": 5,
                    "repairable": True,
                    "detections": [
                        {
                            "class_name": "Bumper",
                            "confidence": 0.96,
                        }
                    ],
                }
            ]

            nlp_data = {
                "accident_type": "Rear-end Collision",
                "vehicle_part": "Rear Bumper",
                "weather": "Clear",
                "severity": "Medium",
                "cause": "Vehicle hit from behind",
            }

            rag_result = """
Policy Verification

✓ Damage is covered under Comprehensive Policy.
✓ Deductible: ₹5,000
✓ Claim Eligible.
"""

            decision_data = {
                "coverage": "Covered",
                "fraud_score": 8,
                "decision": "Approved",
                "reason": "Covered by policy with low fraud risk.",
            }

            crew_report = """
Insurance Claim Executive Report

Executive Summary:
The insurance claim has been successfully processed.

Damage Assessment:
Rear bumper damage detected.

Accident Analysis:
Rear-end collision.

Policy Coverage:
Covered.

Fraud Assessment:
Low Fraud Risk.

Final Decision:
Approved.

Recommendation:
Proceed with claim settlement.
"""

            return {
                "claim_id": claim_id,
                "cv": {
                    "status": "Completed",
                    "images_processed": 1,
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
                "crew_report": crew_report,
            }

        # ==========================================================
        # REAL AI PIPELINE (Local)
        # ==========================================================

        predictions = self.cv.detect_claim(claim_id)

        cv_result = self.cv.save_results(
            db,
            claim_id,
            predictions,
        )

        nlp_result = self.nlp.analyze_claim(
            db,
            claim_id,
        )

        rag_result = self.rag.verify_policy(
            db,
            claim_id,
        )

        decision = self.decision.process_claim(
            db,
            claim_id,
        )

        cv_data = []

        for item in cv_result:

            cv_data.append(
                {
                    "image_name": item.image_name,
                    "severity": item.severity,
                    "repair_cost": item.repair_cost,
                    "repair_days": item.repair_days,
                    "repairable": item.repairable,
                    "detections": item.detections,
                }
            )

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

        crew = InsuranceClaimCrew()

        crew_report = crew.kickoff(
            claim_id=claim_id,
            cv_result=cv_data,
            nlp_result=nlp_data,
            rag_result=rag_result,
            decision_result=decision_data,
        )

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
            "crew_report": crew_report,
        }