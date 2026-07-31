from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database.base import Base


class Claim(Base):
    __tablename__ = "claims"

    claim_id = Column(
        String(20),
        primary_key=True
    )

    customer_id = Column(
        Integer,
        ForeignKey("customers.customer_id"),
        nullable=False
    )

    policy_number = Column(
        String(20),
        ForeignKey("policies.policy_number"),
        nullable=False
    )

    claim_amount = Column(Float)

    claim_status = Column(String(50))

    description = Column(String)

    customer = relationship(
        "Customer",
        back_populates="claims"
    )

    policy = relationship(
        "Policy",
        back_populates="claims"
    )

    ai_decision = relationship(
        "AIDecision",
        back_populates="claim",
        uselist=False
    )