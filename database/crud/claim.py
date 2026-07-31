from sqlalchemy.orm import Session

from database.models.claim import Claim
from database.schemas.claim import ClaimCreate


def create_claim(db: Session, claim: ClaimCreate):
    db_claim = Claim(
        policy_id=claim.policy_id,
        vehicle_id=claim.vehicle_id,
        customer_id=claim.customer_id,
        claim_date=claim.claim_date,
        incident_date=claim.incident_date,
        damage_description=claim.damage_description,
        estimated_amount=claim.estimated_amount,
        claim_status=claim.claim_status
    )

    db.add(db_claim)
    db.commit()
    db.refresh(db_claim)

    return db_claim


def get_claim(db: Session, claim_id: int):
    return (
        db.query(Claim)
        .filter(Claim.claim_id == claim_id)
        .first()
    )


def get_all_claims(db: Session):
    return db.query(Claim).all()


def get_claims_by_customer(db: Session, customer_id: int):
    return (
        db.query(Claim)
        .filter(Claim.customer_id == customer_id)
        .all()
    )


def get_claims_by_policy(db: Session, policy_id: int):
    return (
        db.query(Claim)
        .filter(Claim.policy_id == policy_id)
        .all()
    )


def update_claim(
    db: Session,
    claim_id: int,
    claim: ClaimCreate
):
    db_claim = (
        db.query(Claim)
        .filter(Claim.claim_id == claim_id)
        .first()
    )

    if db_claim is None:
        return None

    db_claim.policy_id = claim.policy_id
    db_claim.vehicle_id = claim.vehicle_id
    db_claim.customer_id = claim.customer_id
    db_claim.claim_date = claim.claim_date
    db_claim.incident_date = claim.incident_date
    db_claim.damage_description = claim.damage_description
    db_claim.estimated_amount = claim.estimated_amount
    db_claim.claim_status = claim.claim_status

    db.commit()
    db.refresh(db_claim)

    return db_claim


def delete_claim(db: Session, claim_id: int):
    db_claim = (
        db.query(Claim)
        .filter(Claim.claim_id == claim_id)
        .first()
    )

    if db_claim is None:
        return None

    db.delete(db_claim)
    db.commit()

    return db_claim