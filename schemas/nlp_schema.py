from pydantic import BaseModel


class NLPRequest(BaseModel):

    claim_id: str

    claim_description: str


class NLPResponse(BaseModel):

    accident_type: str | None = None

    vehicle_part: str | None = None

    weather: str | None = None

    severity: str

    cause: str 