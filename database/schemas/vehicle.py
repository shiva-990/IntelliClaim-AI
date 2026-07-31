from pydantic import BaseModel, ConfigDict
from typing import Optional


class VehicleCreate(BaseModel):
    customer_id: int
    registration_number: str
    make: Optional[str] = None
    model: Optional[str] = None
    manufacture_year: Optional[int] = None


class VehicleResponse(BaseModel):
    vehicle_id: int
    customer_id: int
    registration_number: str
    make: Optional[str] = None
    model: Optional[str] = None
    manufacture_year: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)