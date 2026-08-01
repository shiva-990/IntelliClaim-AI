from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class PolicyCreate(BaseModel):

    policy_number: str
    customer_id: str

    policy_type: str
    insurance_provider: str

    premium_amount: float
    sum_insured: float
    deductible: float

    roadside_assistance: str
    engine_protection: str
    personal_accident_cover: str

    valid_from: date
    valid_to: date

    policy_status: str


class PolicyUpdate(BaseModel):

    customer_id: Optional[str] = None

    policy_type: Optional[str] = None
    insurance_provider: Optional[str] = None

    premium_amount: Optional[float] = None
    sum_insured: Optional[float] = None
    deductible: Optional[float] = None

    roadside_assistance: Optional[str] = None
    engine_protection: Optional[str] = None
    personal_accident_cover: Optional[str] = None

    valid_from: Optional[date] = None
    valid_to: Optional[date] = None

    policy_status: Optional[str] = None


class PolicyResponse(PolicyCreate):

    model_config = ConfigDict(
        from_attributes=True
    )