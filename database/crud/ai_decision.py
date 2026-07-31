from sqlalchemy.orm import Session

from database.models.ai_decision import AIDecision
from database.schemas.ai_decision import AIDecisionCreate


def create_ai_decision(db: Session, decision: AIDecisionCreate):
    db_decision = AIDecision(
        claim_id=decision.claim_id,
        damage_severity=decision.damage_severity,
        estimated_repair_cost=decision.estimated_repair_cost,
        fraud_probability=decision.fraud_probability,
        coverage_status=decision.coverage_status,
        ai_decision=decision.ai_decision,
        confidence_score=decision.confidence_score,
        remarks=decision.remarks
    )

    db.add(db_decision)
    db.commit()
    db.refresh(db_decision)

    return db_decision


def get_ai_decision(db: Session, decision_id: int):
    return (
        db.query(AIDecision)
        .filter(AIDecision.decision_id == decision_id)
        .first()
    )


def get_ai_decision_by_claim(db: Session, claim_id: int):
    return (
        db.query(AIDecision)
        .filter(AIDecision.claim_id == claim_id)
        .first()
    )


def get_all_ai_decisions(db: Session):
    return db.query(AIDecision).all()


def update_ai_decision(
    db: Session,
    decision_id: int,
    decision: AIDecisionCreate
):
    db_decision = (
        db.query(AIDecision)
        .filter(AIDecision.decision_id == decision_id)
        .first()
    )

    if db_decision is None:
        return None

    db_decision.claim_id = decision.claim_id
    db_decision.damage_severity = decision.damage_severity
    db_decision.estimated_repair_cost = decision.estimated_repair_cost
    db_decision.fraud_probability = decision.fraud_probability
    db_decision.coverage_status = decision.coverage_status
    db_decision.ai_decision = decision.ai_decision
    db_decision.confidence_score = decision.confidence_score
    db_decision.remarks = decision.remarks

    db.commit()
    db.refresh(db_decision)

    return db_decision


def delete_ai_decision(db: Session, decision_id: int):
    db_decision = (
        db.query(AIDecision)
        .filter(AIDecision.decision_id == decision_id)
        .first()
    )

    if db_decision is None:
        return None

    db.delete(db_decision)
    db.commit()

    return db_decision