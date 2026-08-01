from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import get_db

from database.schemas.claim import (
    ClaimCreate,
    ClaimUpdate,
    ClaimResponse,
)

from database.crud.claim import (
    create_claim,
    get_claim,
    get_all_claims,
    update_claim,
    delete_claim,
)

router = APIRouter(
    prefix="/claims",
    tags=["Claims"],
)


@router.post(
    "/",
    response_model=ClaimResponse,
)
def create_claim_api(
    claim: ClaimCreate,
    db: Session = Depends(get_db),
):

    existing = get_claim(
        db,
        claim.claim_id,
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Claim already exists",
        )

    return create_claim(
        db,
        claim,
    )


@router.get(
    "/",
    response_model=list[ClaimResponse],
)
def get_all_claims_api(
    db: Session = Depends(get_db),
):
    return get_all_claims(db)


@router.get(
    "/{claim_id}",
    response_model=ClaimResponse,
)
def get_claim_api(
    claim_id: str,
    db: Session = Depends(get_db),
):

    claim = get_claim(
        db,
        claim_id,
    )

    if claim is None:
        raise HTTPException(
            status_code=404,
            detail="Claim not found",
        )

    return claim


@router.put(
    "/{claim_id}",
    response_model=ClaimResponse,
)
def update_claim_api(
    claim_id: str,
    claim: ClaimUpdate,
    db: Session = Depends(get_db),
):

    updated = update_claim(
        db,
        claim_id,
        claim,
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Claim not found",
        )

    return updated


@router.delete(
    "/{claim_id}",
)
def delete_claim_api(
    claim_id: str,
    db: Session = Depends(get_db),
):

    deleted = delete_claim(
        db,
        claim_id,
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Claim not found",
        )

    return {
        "message": "Claim deleted successfully"
    }