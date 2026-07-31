from pydantic import BaseModel, ConfigDict
from typing import Optional


class PolicyCreate(BaseModel):
    policy_number: str
    customer_id: int
    policy_type: Optional[str] = None
    premium_amount: Optional[float] = None
    sum_insured: Optional[float] = None


class PolicyResponse(BaseModel):
    policy_number: str
    customer_id: int
    policy_type: Optional[str] = None
    premium_amount: Optional[float] = None
    sum_insured: Optional[float] = None

    model_config = ConfigDict(from_attributes=True)