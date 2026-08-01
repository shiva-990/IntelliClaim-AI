from pydantic import BaseModel, ConfigDict
from typing import Optional


class CustomerCreate(BaseModel):

    customer_id: str
    customer_name: str
    age: int
    gender: str
    phone: str
    email: str

    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    pincode: Optional[str] = None
    driving_license_no: Optional[str] = None


class CustomerUpdate(BaseModel):

    customer_name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    pincode: Optional[str] = None
    driving_license_no: Optional[str] = None


class CustomerResponse(CustomerCreate):

    model_config = ConfigDict(
        from_attributes=True
    )