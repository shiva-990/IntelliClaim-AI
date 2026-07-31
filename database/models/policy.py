from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database.base import Base


class Policy(Base):
    __tablename__ = "policies"

    policy_number = Column(
        String(20),
        primary_key=True
    )

    customer_id = Column(
        Integer,
        ForeignKey("customers.customer_id"),
        nullable=False
    )

    policy_type = Column(String(50))

    premium_amount = Column(Float)

    sum_insured = Column(Float)

    customer = relationship(
        "Customer",
        back_populates="policies"
    )

    claims = relationship(
        "Claim",
        back_populates="policy"
    )