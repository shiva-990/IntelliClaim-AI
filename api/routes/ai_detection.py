from fastapi import APIRouter, HTTPException

from api.deps import DBSession

from database.crud.ai_detection import (
    create_ai_detection,
    get_ai_detection,
    get_ai_detection_by_claim,
    get_all_ai_detections,
)

from database.schemas.ai_detection import (
    AIDetectionCreate,
    AIDetectionResponse,
)

router = APIRouter(
    prefix="/ai-detections",
    tags=["AI Detection"],
)


@router.post("/", response_model=AIDetectionResponse)
def create_detection_api(
    detection: AIDetectionCreate,
    db: DBSession,
):
    return create_ai_detection(db, detection)


@router.get("/", response_model=list[AIDetectionResponse])
def get_all_detections_api(
    db: DBSession,
):
    return get_all_ai_detections(db)


@router.get("/{detection_id}", response_model=AIDetectionResponse)
def get_detection_api(
    detection_id: int,
    db: DBSession,
):
    detection = get_ai_detection(
        db,
        detection_id,
    )

    if detection is None:
        raise HTTPException(
            status_code=404,
            detail="Detection not found",
        )

    return detection


@router.get(
    "/claim/{claim_id}",
    response_model=list[AIDetectionResponse],
)
def get_detection_by_claim_api(
    claim_id: int,
    db: DBSession,
):
    return get_ai_detection_by_claim(
        db,
        claim_id,
    )