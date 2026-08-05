from database.crud.claim import get_claim

from database.crud.ai_detection import (
    get_ai_detection_by_claim,
)

from database.crud.nlp_analysis import (
    get_nlp_analysis,
)

from database.crud.ai_decision import (
    create_ai_decision,
    get_ai_decision_by_claim,
)

from database.schemas.ai_decision import (
    AIDecisionCreate,
)

from rag.services.rag_service import (
    RAGService,
)


class DecisionService:

    def __init__(self):

        self.rag = RAGService()

    def process_claim(
        self,
        db,
        claim_id: str,
    ):

        # ---------------------------------
        # Get Claim
        # ---------------------------------
        claim = get_claim(
            db,
            claim_id,
        )

        if claim is None:
            raise Exception(
                "Claim not found."
            )

        # ---------------------------------
        # Check Existing Decision
        # ---------------------------------
        existing = get_ai_decision_by_claim(
            db,
            claim_id,
        )

        if existing:
            print(f"[Decision] Existing decision found for {claim_id}")
            return existing

        # ---------------------------------
        # Get CV Detection
        # ---------------------------------
        detection = get_ai_detection_by_claim(
            db,
            claim_id,
        )

        # ---------------------------------
        # Get NLP Analysis
        # ---------------------------------
        nlp = get_nlp_analysis(
            db,
            claim_id,
        )

        # ---------------------------------
        # Get RAG Result
        # ---------------------------------
        rag_answer = self.rag.verify_policy(
            db,
            claim_id,
        )

        print(f"[Decision] RAG Response: {rag_answer}")

        # ---------------------------------
        # Coverage Decision
        # ---------------------------------
        coverage = "Not Covered"

        answer = rag_answer.lower()

        if "covered" in answer or "yes" in answer:
            coverage = "Covered"

        # ---------------------------------
        # Fraud Score
        # ---------------------------------
        fraud_score = (
            claim.fraud_score
            if claim.fraud_score is not None
            else 0.0
        )

        # ---------------------------------
        # Initial Decision
        # ---------------------------------
        decision = "Manual Review"

        reasons = []

        # Rule 1
        if coverage == "Covered":

            decision = "Approve"

            reasons.append(
                "Policy covers the reported damage."
            )

        else:

            decision = "Reject"

            reasons.append(
                "Policy does not cover the reported damage."
            )

        # Rule 2
        if fraud_score >= 80:

            decision = "Manual Review"

            reasons.append(
                "High fraud score detected."
            )

        # Rule 3
        if claim.claim_amount > 500000:

            decision = "Manual Review"

            reasons.append(
                "High claim amount requires manual verification."
            )

        # Rule 4
        if not detection:

            reasons.append(
                "CV analysis not available."
            )

        # Rule 5
        if nlp is None:

            reasons.append(
                "NLP analysis not available."
            )

        # ---------------------------------
        # Save Decision
        # ---------------------------------
        ai_decision = AIDecisionCreate(

            claim_id=claim.claim_id,

            coverage=coverage,

            fraud_score=fraud_score,

            decision=decision,

            reason=" | ".join(reasons),
        )

        saved = create_ai_decision(
            db,
            ai_decision,
        )

        print(f"[Decision] Decision saved for {claim_id}")

        return saved