from pydantic import BaseModel


class DamageAnalysisResponse(BaseModel):
    severity: str
    repair_cost: float
    repair_days: int
    repairable: bool