from pydantic import BaseModel, ConfigDict
from typing import Optional


class VehicleCreate(BaseModel):
    customer_id: str
    registration_number: str
    make: Optional[str] = None
    model: Optional[str] = None
    manufacture_year: Optional[int] = None


class VehicleUpdate(BaseModel):
    customer_id: Optional[str] = None
    registration_number: Optional[str] = None
    make: Optional[str] = None
    model: Optional[str] = None
    manufacture_year: Optional[int] = None


class VehicleResponse(BaseModel):
    vehicle_id: int
    customer_id: str
    registration_number: str
    make: Optional[str] = None
    model: Optional[str] = None
    manufacture_year: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)