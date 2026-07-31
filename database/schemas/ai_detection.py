from datetime import datetime

from pydantic import BaseModel, ConfigDict


class AIDetectionCreate(BaseModel):
    claim_id: int
    image_name: str
    detections: list[dict]
    severity: str
    repair_cost: float
    repair_days: int
    repairable: bool


class AIDetectionResponse(AIDetectionCreate):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)