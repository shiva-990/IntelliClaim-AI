from pydantic import BaseModel


class Detection(BaseModel):
    part: str
    confidence: float
    bbox: list[float]


class DetectionResponse(BaseModel):
    filename: str
    detections: list[Detection]