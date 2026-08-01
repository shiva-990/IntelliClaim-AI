from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from database.base import Base
from sqlalchemy import DateTime
from sqlalchemy.sql import func

class Customer(Base):

    __tablename__ = "customers"

    customer_id = Column(
        String(20),
        primary_key=True,
        index=True
    )

    customer_name = Column(
        String(100),
        nullable=False
    )

    age = Column(
        Integer,
        nullable=False
    )

    gender = Column(
        String(20),
        nullable=False
    )

    phone = Column(
        String(20),
        unique=True,
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    address = Column(String(255))

    city = Column(String(100))

    state = Column(String(100))

    pincode = Column(String(10))

    driving_license_no = Column(
        String(30),
        unique=True
    )

    policies = relationship(
        "Policy",
        back_populates="customer"
    )

    claims = relationship(
        "Claim",
        back_populates="customer"
    )
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
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