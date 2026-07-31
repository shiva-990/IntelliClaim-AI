from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.base import Base


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)

    customer_name = Column(String(100), nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    phone = Column(String(20), unique=True, nullable=False)

    address = Column(String(255))

    policies = relationship(
        "Policy",
        back_populates="customer"
    )

    claims = relationship(
        "Claim",
        back_populates="customer"
    )

    vehicles = relationship(
        "Vehicle",
        back_populates="customer"
    )