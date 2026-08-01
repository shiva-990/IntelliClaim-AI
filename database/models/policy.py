from sqlalchemy import (
    Column,
    String,
    Float,
    Date,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from database.base import Base
from sqlalchemy import DateTime
from sqlalchemy.sql import func

class Policy(Base):

    __tablename__ = "policies"

    policy_number = Column(
        String(20),
        primary_key=True,
        index=True,
    )

    customer_id = Column(
        String(20),
        ForeignKey("customers.customer_id"),
        nullable=False,
    )

    policy_type = Column(
        String(50),
        nullable=False,
    )

    insurance_provider = Column(
        String(100),
        nullable=False,
    )

    premium_amount = Column(
        Float,
        nullable=False,
    )

    sum_insured = Column(
        Float,
        nullable=False,
    )

    deductible = Column(
        Float,
        nullable=False,
    )

    roadside_assistance = Column(
        String(10),
        nullable=False,
    )

    engine_protection = Column(
        String(10),
        nullable=False,
    )

    personal_accident_cover = Column(
        String(10),
        nullable=False,
    )

    valid_from = Column(
        Date,
        nullable=False,
    )

    valid_to = Column(
        Date,
        nullable=False,
    )

    policy_status = Column(
        String(20),
        nullable=False,
    )

    customer = relationship(
        "Customer",
        back_populates="policies",
    )

    claims = relationship(
        "Claim",
        back_populates="policy",
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