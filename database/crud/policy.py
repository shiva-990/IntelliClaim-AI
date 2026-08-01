from sqlalchemy.orm import Session

from database.models.policy import Policy
from database.schemas.policy import (
    PolicyCreate,
    PolicyUpdate,
)


def create_policy(db: Session, policy: PolicyCreate):

    db_policy = Policy(**policy.model_dump())

    db.add(db_policy)
    db.commit()
    db.refresh(db_policy)

    return db_policy


def get_policy(
    db: Session,
    policy_number: str,
):
    return (
        db.query(Policy)
        .filter(
            Policy.policy_number == policy_number
        )
        .first()
    )


def get_all_policies(db: Session):
    return db.query(Policy).all()


def update_policy(
    db: Session,
    policy_number: str,
    policy: PolicyUpdate,
):

    db_policy = get_policy(
        db,
        policy_number,
    )

    if db_policy is None:
        return None

    update_data = policy.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(db_policy, key, value)

    db.commit()
    db.refresh(db_policy)

    return db_policy


def delete_policy(
    db: Session,
    policy_number: str,
):

    db_policy = get_policy(
        db,
        policy_number,
    )

    if db_policy is None:
        return None

    db.delete(db_policy)
    db.commit()

    return db_policy