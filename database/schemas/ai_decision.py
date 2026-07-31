from pydantic import BaseModel, ConfigDict
from typing import Optional


class AIDecisionCreate(BaseModel):
    claim_id: str
    coverage: Optional[str] = None
    fraud_score: Optional[float] = None
    decision: Optional[str] = None
    reason: Optional[str] = None


class AIDecisionResponse(BaseModel):
    decision_id: int
    claim_id: str
    coverage: Optional[str] = None
    fraud_score: Optional[float] = None
    decision: Optional[str] = None
    reason: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)