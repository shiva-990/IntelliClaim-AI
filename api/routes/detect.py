from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import get_db

from cv.services.detection_service import DetectionService

from database.crud.claim import get_claim

router = APIRouter(
    prefix="/detect",
    tags=["Damage Detection"],
)


@router.post("/damage/{claim_id}")
def detect_damage(
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

    service = DetectionService()

    try:

        predictions = service.detect_claim(
            claim_id
        )

        saved = service.save_results(
            db,
            claim_id,
            predictions,
        )

        return {
            "claim_id": claim_id,
            "images_processed": len(predictions),
            "detections_saved": len(saved),
            "cv_status": "Completed",
        }

    except FileNotFoundError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )