from fastapi import APIRouter, HTTPException

from api.deps import DBSession
from database.crud import ai_decision as ai_decision_crud
from database.schemas.ai_decision import (
    AIDecisionCreate,
    AIDecisionResponse,
)

router = APIRouter(
    prefix="/ai-decisions",
    tags=["AI Decisions"]
)


@router.post("/", response_model=AIDecisionResponse)
def create_ai_decision_api(
    decision: AIDecisionCreate,
    db: DBSession
):
    return ai_decision_crud.create_ai_decision(db, decision)


@router.get("/", response_model=list[AIDecisionResponse])
def get_all_ai_decisions_api(
    db: DBSession
):
    return ai_decision_crud.get_all_ai_decisions(db)


@router.get("/claim/{claim_id}", response_model=AIDecisionResponse)
def get_ai_decision_by_claim_api(
    claim_id: int,
    db: DBSession
):
    decision = ai_decision_crud.get_ai_decision_by_claim(
        db,
        claim_id
    )

    if decision is None:
        raise HTTPException(
            status_code=404,
            detail="AI Decision not found"
        )

    return decision


@router.get("/{decision_id}", response_model=AIDecisionResponse)
def get_ai_decision_api(
    decision_id: int,
    db: DBSession
):
    decision = ai_decision_crud.get_ai_decision(
        db,
        decision_id
    )

    if decision is None:
        raise HTTPException(
            status_code=404,
            detail="AI Decision not found"
        )

    return decision


@router.put("/{decision_id}", response_model=AIDecisionResponse)
def update_ai_decision_api(
    decision_id: int,
    decision: AIDecisionCreate,
    db: DBSession
):
    updated_decision = ai_decision_crud.update_ai_decision(
        db,
        decision_id,
        decision
    )

    if updated_decision is None:
        raise HTTPException(
            status_code=404,
            detail="AI Decision not found"
        )

    return updated_decision


@router.delete("/{decision_id}")
def delete_ai_decision_api(
    decision_id: int,
    db: DBSession
):
    deleted_decision = ai_decision_crud.delete_ai_decision(
        db,
        decision_id
    )

    if deleted_decision is None:
        raise HTTPException(
            status_code=404,
            detail="AI Decision not found"
        )

    return {
        "message": "AI Decision deleted successfully"
    }