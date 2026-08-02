from sqlalchemy.orm import Session

from database.models.ai_decision import AIDecision
from database.schemas.ai_decision import AIDecisionCreate


def create_ai_decision(
    db: Session,
    decision: AIDecisionCreate,
):

    db_decision = AIDecision(
        **decision.model_dump()
    )

    db.add(db_decision)

    db.commit()

    db.refresh(db_decision)

    return db_decision


def get_ai_decision(
    db: Session,
    decision_id: int,
):

    return (
        db.query(AIDecision)
        .filter(
            AIDecision.decision_id == decision_id
        )
        .first()
    )


def get_ai_decision_by_claim(
    db: Session,
    claim_id: str,
):

    return (
        db.query(AIDecision)
        .filter(
            AIDecision.claim_id == claim_id
        )
        .first()
    )


def get_all_ai_decisions(
    db: Session,
):

    return db.query(AIDecision).all()


def update_ai_decision(
    db: Session,
    decision_id: int,
    decision: AIDecisionCreate,
):

    db_decision = get_ai_decision(
        db,
        decision_id,
    )

    if db_decision is None:

        return None

    update_data = decision.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():

        setattr(
            db_decision,
            key,
            value,
        )

    db.commit()

    db.refresh(db_decision)

    return db_decision


def delete_ai_decision(
    db: Session,
    decision_id: int,
):

    db_decision = get_ai_decision(
        db,
        decision_id,
    )

    if db_decision is None:

        return None

    db.delete(db_decision)

    db.commit()

    return db_decision