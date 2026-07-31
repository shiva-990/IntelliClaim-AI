from sqlalchemy.orm import Session

from database.models.policy import Policy
from database.schemas.policy import PolicyCreate


def create_policy(db: Session, policy: PolicyCreate):
    db_policy = Policy(
        customer_id=policy.customer_id,
        policy_number=policy.policy_number,
        policy_type=policy.policy_type,
        coverage_amount=policy.coverage_amount,
        premium_amount=policy.premium_amount,
        start_date=policy.start_date,
        end_date=policy.end_date,
        status=policy.status
    )

    db.add(db_policy)
    db.commit()
    db.refresh(db_policy)

    return db_policy


def get_policy(db: Session, policy_id: int):
    return (
        db.query(Policy)
        .filter(Policy.policy_id == policy_id)
        .first()
    )


def get_policy_by_number(db: Session, policy_number: str):
    return (
        db.query(Policy)
        .filter(Policy.policy_number == policy_number)
        .first()
    )


def get_all_policies(db: Session):
    return db.query(Policy).all()


def update_policy(
    db: Session,
    policy_id: int,
    policy: PolicyCreate
):
    db_policy = (
        db.query(Policy)
        .filter(Policy.policy_id == policy_id)
        .first()
    )

    if db_policy is None:
        return None

    db_policy.customer_id = policy.customer_id
    db_policy.policy_number = policy.policy_number
    db_policy.policy_type = policy.policy_type
    db_policy.coverage_amount = policy.coverage_amount
    db_policy.premium_amount = policy.premium_amount
    db_policy.start_date = policy.start_date
    db_policy.end_date = policy.end_date
    db_policy.status = policy.status

    db.commit()
    db.refresh(db_policy)

    return db_policy


def delete_policy(db: Session, policy_id: int):
    db_policy = (
        db.query(Policy)
        .filter(Policy.policy_id == policy_id)
        .first()
    )

    if db_policy is None:
        return None

    db.delete(db_policy)
    db.commit()

    return db_policy