from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ClaimCreate(BaseModel):

    claim_id: str
    customer_id: str
    policy_number: str

    accident_date: date
    claim_date: date

    damage_type: str
    accident_description: str

    estimated_repair_cost: float
    claim_amount: float

    fraud_label: str
    fraud_score: int

    claim_status: str
    inspection_status: str
    cv_status: str
    nlp_status: str
    rag_status: str
    final_decision: str


class ClaimUpdate(BaseModel):

    accident_date: Optional[date] = None
    claim_date: Optional[date] = None

    damage_type: Optional[str] = None
    accident_description: Optional[str] = None

    estimated_repair_cost: Optional[float] = None
    claim_amount: Optional[float] = None

    fraud_label: Optional[str] = None
    fraud_score: Optional[int] = None

    claim_status: Optional[str] = None
    inspection_status: Optional[str] = None
    cv_status: Optional[str] = None
    nlp_status: Optional[str] = None
    rag_status: Optional[str] = None
    final_decision: Optional[str] = None


class ClaimResponse(ClaimCreate):

    model_config = ConfigDict(
        from_attributes=True
    )