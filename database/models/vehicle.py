from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from database.base import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    vehicle_id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(
        String(20),
        ForeignKey("customers.customer_id"),
        nullable=False
    )

    registration_number = Column(
        String(20),
        unique=True,
        nullable=False
    )

    make = Column(String(50))

    model = Column(String(50))

    manufacture_year = Column(Integer)

    customer = relationship(
        "Customer",
        back_populates="vehicles"
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
    