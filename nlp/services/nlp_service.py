from database.schemas.nlp_analysis import NLPAnalysisCreate

from database.crud.nlp_analysis import (
    create_nlp_analysis,
    get_nlp_analysis,
)

from database.crud.claim import (
    get_claim,
    update_nlp_status,
)

from nlp.services.extractor import Extractor


class NLPService:

    def __init__(self):
        self.extractor = Extractor()

    def analyze_claim(
        self,
        db,
        claim_id: str,
    ):

        # --------------------------
        # Get Claim
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
        # Check Existing NLP Analysis
        # --------------------------
        existing = get_nlp_analysis(
            db,
            claim_id,
        )

        if existing:
            return existing

        # --------------------------
        # Run NLP Extraction
        # --------------------------
        analysis = self.extractor.extract(
            claim.accident_description
        )

        # --------------------------
        # Create Schema
        # --------------------------
        db_analysis = NLPAnalysisCreate(

            claim_id=claim_id,

            accident_type=analysis.accident_type,

            vehicle_part=analysis.vehicle_part,

            weather=analysis.weather,

            severity=analysis.severity,

            cause=analysis.cause,
        )

        # --------------------------
        # Save Analysis
        # --------------------------
        saved = create_nlp_analysis(
            db,
            db_analysis,
        )

        # --------------------------
        # Update Claim Status
        # --------------------------
        update_nlp_status(
            db,
            claim_id,
            "Completed",
        )

        return saved