from sqlalchemy.orm import Session

from database.models.ai_detection import AIDetection
from database.schemas.ai_detection import AIDetectionCreate


def create_ai_detection(
    db: Session,
    detection: AIDetectionCreate,
):
    db_detection = AIDetection(
        **detection.model_dump()
    )

    db.add(db_detection)
    db.commit()
    db.refresh(db_detection)

    return db_detection


def get_ai_detection(
    db: Session,
    detection_id: int,
):
    return (
        db.query(AIDetection)
        .filter(AIDetection.id == detection_id)
        .first()
    )


def get_ai_detection_by_claim(
    db: Session,
    claim_id: str,
):
    return (
        db.query(AIDetection)
        .filter(AIDetection.claim_id == claim_id)
        .all()
    )


def get_all_ai_detections(db: Session):
    return db.query(AIDetection).all()