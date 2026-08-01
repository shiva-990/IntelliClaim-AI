from datetime import datetime

from pydantic import BaseModel, ConfigDict


class NLPAnalysisCreate(BaseModel):

    claim_id: str

    accident_type: str | None = None

    vehicle_part: str | None = None

    weather: str | None = None

    severity: str

    cause: str


class NLPAnalysisResponse(NLPAnalysisCreate):

    id: int

    created_at: datetime

    model_config = ConfigDict(from_attributes=True) 