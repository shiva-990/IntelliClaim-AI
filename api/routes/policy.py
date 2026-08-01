from fastapi import APIRouter, HTTPException

from api.deps import DBSession

from database.crud.policy import (
    create_policy,
    get_policy,
    get_all_policies,
    update_policy,
    delete_policy,
)

from database.schemas.policy import (
    PolicyCreate,
    PolicyUpdate,
    PolicyResponse,
)

router = APIRouter(
    prefix="/policies",
    tags=["Policies"],
)


@router.post("/", response_model=PolicyResponse)
def create_policy_api(
    policy: PolicyCreate,
    db: DBSession,
):
    return create_policy(db, policy)


@router.get("/", response_model=list[PolicyResponse])
def get_all_policies_api(
    db: DBSession,
):
    return get_all_policies(db)


@router.get("/{policy_number}", response_model=PolicyResponse)
def get_policy_api(
    policy_number: str,
    db: DBSession,
):

    policy = get_policy(
        db,
        policy_number,
    )

    if policy is None:
        raise HTTPException(
            status_code=404,
            detail="Policy not found",
        )

    return policy


@router.put("/{policy_number}", response_model=PolicyResponse)
def update_policy_api(
    policy_number: str,
    policy: PolicyUpdate,
    db: DBSession,
):

    updated = update_policy(
        db,
        policy_number,
        policy,
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Policy not found",
        )

    return updated


@router.delete("/{policy_number}")
def delete_policy_api(
    policy_number: str,
    db: DBSession,
):

    deleted = delete_policy(
        db,
        policy_number,
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Policy not found",
        )

    return {
        "message": "Policy deleted successfully"
    }