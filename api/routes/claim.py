from fastapi import APIRouter, HTTPException

from api.deps import DBSession
from database.crud import claim as claim_crud
from database.schemas.claim import (
    ClaimCreate,
    ClaimResponse,
)

router = APIRouter(
    prefix="/claims",
    tags=["Claims"]
)


@router.post("/", response_model=ClaimResponse)
def create_claim_api(
    claim: ClaimCreate,
    db: DBSession
):
    return claim_crud.create_claim(db, claim)


@router.get("/", response_model=list[ClaimResponse])
def get_all_claims_api(
    db: DBSession
):
    return claim_crud.get_all_claims(db)


@router.get("/customer/{customer_id}", response_model=list[ClaimResponse])
def get_claims_by_customer_api(
    customer_id: int,
    db: DBSession
):
    return claim_crud.get_claims_by_customer(
        db,
        customer_id
    )


@router.get("/policy/{policy_id}", response_model=list[ClaimResponse])
def get_claims_by_policy_api(
    policy_id: int,
    db: DBSession
):
    return claim_crud.get_claims_by_policy(
        db,
        policy_id
    )


@router.get("/{claim_id}", response_model=ClaimResponse)
def get_claim_api(
    claim_id: int,
    db: DBSession
):
    claim = claim_crud.get_claim(
        db,
        claim_id
    )

    if claim is None:
        raise HTTPException(
            status_code=404,
            detail="Claim not found"
        )

    return claim


@router.put("/{claim_id}", response_model=ClaimResponse)
def update_claim_api(
    claim_id: int,
    claim: ClaimCreate,
    db: DBSession
):
    updated_claim = claim_crud.update_claim(
        db,
        claim_id,
        claim
    )

    if updated_claim is None:
        raise HTTPException(
            status_code=404,
            detail="Claim not found"
        )

    return updated_claim


@router.delete("/{claim_id}")
def delete_claim_api(
    claim_id: int,
    db: DBSession
):
    deleted_claim = claim_crud.delete_claim(
        db,
        claim_id
    )

    if deleted_claim is None:
        raise HTTPException(
            status_code=404,
            detail="Claim not found"
        )

    return {
        "message": "Claim deleted successfully"
    }