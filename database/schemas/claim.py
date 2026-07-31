from pydantic import BaseModel, ConfigDict
from typing import Optional


class ClaimCreate(BaseModel):
    claim_id: str
    customer_id: int
    policy_number: str
    claim_amount: Optional[float] = None
    claim_status: Optional[str] = None
    description: Optional[str] = None


class ClaimResponse(BaseModel):
    claim_id: str
    customer_id: int
    policy_number: str
    claim_amount: Optional[float] = None
    claim_status: Optional[str] = None
    description: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)