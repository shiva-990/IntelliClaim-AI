from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional


class CustomerCreate(BaseModel):
    customer_name: str
    email: EmailStr
    phone: str
    address: Optional[str] = None


class CustomerResponse(BaseModel):
    customer_id: int
    customer_name: str
    email: EmailStr
    phone: str
    address: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)