from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import get_db

from database.crud.claim import get_claim

from nlp.services.nlp_service import NLPService

router = APIRouter(
    prefix="/nlp",
    tags=["NLP Analysis"],
)


@router.post("/analyze/{claim_id}")
def analyze_claim(
    claim_id: str,
    db: Session = Depends(get_db),
):

    claim = get_claim(
        db,
        claim_id,
    )

    if claim is None:
        raise HTTPException(
            status_code=404,
            detail="Claim not found",
        )

    try:

        service = NLPService()

        analysis = service.analyze_claim(
            db,
            claim_id,
        )

        return {

            "claim_id": claim_id,

            "accident_type": analysis.accident_type,

            "vehicle_part": analysis.vehicle_part,

            "weather": analysis.weather,

            "severity": analysis.severity,

            "cause": analysis.cause,

            "nlp_status": "Completed",
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )