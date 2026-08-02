from fastapi import APIRouter, HTTPException

from api.deps import DBSession

from services.claim_processing_service import (
    ClaimProcessingService,
)

router = APIRouter(
    prefix="/process",
    tags=["Claim Processing"],
)

service = ClaimProcessingService()


@router.post("/{claim_id}")
def process_claim(
    claim_id: str,
    db: DBSession,
):

    try:

        return service.process_claim(
            db,
            claim_id,
        )

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )