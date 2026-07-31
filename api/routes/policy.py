from fastapi import APIRouter, HTTPException

from api.deps import DBSession
from database.crud import policy as policy_crud
from database.schemas.policy import (
    PolicyCreate,
    PolicyResponse,
)

router = APIRouter(
    prefix="/policies",
    tags=["Policies"]
)


@router.post("/", response_model=PolicyResponse)
def create_policy_api(
    policy: PolicyCreate,
    db: DBSession
):
    return policy_crud.create_policy(db, policy)


@router.get("/", response_model=list[PolicyResponse])
def get_all_policies_api(
    db: DBSession
):
    return policy_crud.get_all_policies(db)


@router.get("/{policy_id}", response_model=PolicyResponse)
def get_policy_api(
    policy_id: int,
    db: DBSession
):
    policy = policy_crud.get_policy(db, policy_id)

    if policy is None:
        raise HTTPException(
            status_code=404,
            detail="Policy not found"
        )

    return policy


@router.get("/number/{policy_number}", response_model=PolicyResponse)
def get_policy_by_number_api(
    policy_number: str,
    db: DBSession
):
    policy = policy_crud.get_policy_by_number(
        db,
        policy_number
    )

    if policy is None:
        raise HTTPException(
            status_code=404,
            detail="Policy not found"
        )

    return policy


@router.put("/{policy_id}", response_model=PolicyResponse)
def update_policy_api(
    policy_id: int,
    policy: PolicyCreate,
    db: DBSession
):
    updated_policy = policy_crud.update_policy(
        db,
        policy_id,
        policy
    )

    if updated_policy is None:
        raise HTTPException(
            status_code=404,
            detail="Policy not found"
        )

    return updated_policy


@router.delete("/{policy_id}")
def delete_policy_api(
    policy_id: int,
    db: DBSession
):
    deleted_policy = policy_crud.delete_policy(
        db,
        policy_id
    )

    if deleted_policy is None:
        raise HTTPException(
            status_code=404,
            detail="Policy not found"
        )

    return {
        "message": "Policy deleted successfully"
    }