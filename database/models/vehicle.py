from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.base import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    vehicle_id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(
        Integer,
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