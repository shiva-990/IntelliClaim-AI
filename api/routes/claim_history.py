from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from database.session import get_db

from database.crud.claim import (
    get_claim_history,
    get_claim,
)

router = APIRouter(
    prefix="/claims",
    tags=["Claim History"],
)


# --------------------------------------------------
# Claim History
# --------------------------------------------------

@router.get("")
def claim_history(
    db: Session = Depends(get_db),
):

    claims = get_claim_history(db)

    response = []

    for claim in claims:

        response.append(
            {
                "claim_id": claim.claim_id,
                "customer_id": claim.customer_id,
                "policy_number": claim.policy_number,
                "claim_date": claim.claim_date,
                "claim_status": claim.claim_status,
                "final_decision": claim.final_decision,
                "cv_status": claim.cv_status,
                "nlp_status": claim.nlp_status,
                "rag_status": claim.rag_status,
                "created_at": claim.created_at,
            }
        )

    return response


# --------------------------------------------------
# Claim Details
# --------------------------------------------------

@router.get("/{claim_id}")
def claim_details(
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

    return {
        "claim_id": claim.claim_id,
        "customer_id": claim.customer_id,
        "policy_number": claim.policy_number,
        "accident_date": claim.accident_date,
        "claim_date": claim.claim_date,
        "damage_type": claim.damage_type,
        "accident_description": claim.accident_description,
        "estimated_repair_cost": claim.estimated_repair_cost,
        "claim_amount": claim.claim_amount,
        "claim_status": claim.claim_status,
        "final_decision": claim.final_decision,
        "cv_status": claim.cv_status,
        "nlp_status": claim.nlp_status,
        "rag_status": claim.rag_status,
        "inspection_status": claim.inspection_status,
        "fraud_label": claim.fraud_label,
        "fraud_score": claim.fraud_score,
        "created_at": claim.created_at,
    }