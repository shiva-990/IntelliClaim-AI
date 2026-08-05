from database.crud.ai_detection import get_ai_detection_by_claim
from database.crud.nlp_analysis import get_nlp_analysis
from database.crud.ai_decision import get_ai_decision_by_claim


class ReportService:

    def build_report(
        self,
        db,
        claim_id: str,
    ):

        detection = get_ai_detection_by_claim(
            db,
            claim_id,
        )

        nlp = get_nlp_analysis(
            db,
            claim_id,
        )

        decision = get_ai_decision_by_claim(
            db,
            claim_id,
        )

        cv_data = []

        for item in detection:

            cv_data.append({

                "image_name": item.image_name,

                "detections": item.detections,

                "severity": item.severity,

                "repair_cost": item.repair_cost,

                "repair_days": item.repair_days,

                "repairable": item.repairable,

            })

        nlp_data = None

        if nlp:

            nlp_data = {

                "accident_type": nlp.accident_type,

                "vehicle_part": nlp.vehicle_part,

                "weather": nlp.weather,

                "severity": nlp.severity,

                "cause": nlp.cause,

            }

        decision_data = None

        if decision:

            decision_data = {

                "coverage": decision.coverage,

                "fraud_score": decision.fraud_score,

                "decision": decision.decision,

                "reason": decision.reason,

            }

        return {

            "claim_id": claim_id,

            "cv": cv_data,

            "nlp": nlp_data,

            "decision": decision_data,

        }