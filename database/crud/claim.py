from sqlalchemy.orm import Session

from database.models.claim import Claim
from database.schemas.claim import (
    ClaimCreate,
    ClaimUpdate,
)


def create_claim(
    db: Session,
    claim: ClaimCreate,
):
    db_claim = Claim(**claim.model_dump())

    db.add(db_claim)
    db.commit()
    db.refresh(db_claim)

    return db_claim


def get_claim(
    db: Session,
    claim_id: str,
):
    return (
        db.query(Claim)
        .filter(Claim.claim_id == claim_id)
        .first()
    )


def get_all_claims(
    db: Session,
):
    return db.query(Claim).all()


def get_claims_by_customer(
    db: Session,
    customer_id: str,
):
    return (
        db.query(Claim)
        .filter(Claim.customer_id == customer_id)
        .all()
    )


def get_claims_by_policy(
    db: Session,
    policy_number: str,
):
    return (
        db.query(Claim)
        .filter(Claim.policy_number == policy_number)
        .all()
    )


def update_claim(
    db: Session,
    claim_id: str,
    claim: ClaimUpdate,
):
    db_claim = get_claim(
        db,
        claim_id,
    )

    if db_claim is None:
        return None

    update_data = claim.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(
            db_claim,
            key,
            value,
        )

    db.commit()
    db.refresh(db_claim)

    return db_claim


def delete_claim(
    db: Session,
    claim_id: str,
):
    db_claim = get_claim(
        db,
        claim_id,
    )

    if db_claim is None:
        return None

    db.delete(db_claim)
    db.commit()

    return db_claim

def update_cv_status(
    db: Session,
    claim_id: str,
    status: str,
):

    claim = get_claim(
        db,
        claim_id,
    )

    if claim is None:
        return None

    claim.cv_status = status

    db.commit()

    db.refresh(claim)

    return claim

def update_cv_status(
    db: Session,
    claim_id: str,
    status: str,
):

    claim = get_claim(
        db,
        claim_id,
    )

    if claim is None:
        return None

    claim.cv_status = status

    db.commit()

    db.refresh(claim)

    return claim

def update_cv_status(
    db: Session,
    claim_id: str,
    status: str,
):

    claim = (
        db.query(Claim)
        .filter(Claim.claim_id == claim_id)
        .first()
    )

    if claim is None:
        return None

    claim.cv_status = status

    db.commit()
    db.refresh(claim)

    return claim

def update_nlp_status(
    db: Session,
    claim_id: str,
    status: str,
):

    claim = (
        db.query(Claim)
        .filter(
            Claim.claim_id == claim_id
        )
        .first()
    )

    if claim is None:
        return None

    claim.nlp_status = status

    db.commit()

    db.refresh(claim)

    return claim