from sqlalchemy import (
    Column,
    String,
    Float,
    Integer,
    Date,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from database.base import Base
from sqlalchemy import DateTime
from sqlalchemy.sql import func

class Claim(Base):

    __tablename__ = "claims"

    claim_id = Column(
        String(20),
        primary_key=True,
        index=True,
    )

    customer_id = Column(
        String(20),
        ForeignKey("customers.customer_id"),
        nullable=False,
    )

    policy_number = Column(
        String(20),
        ForeignKey("policies.policy_number"),
        nullable=False,
    )

    accident_date = Column(
        Date,
        nullable=False,
    )

    claim_date = Column(
        Date,
        nullable=False,
    )

    damage_type = Column(
        String(50),
        nullable=False,
    )

    accident_description = Column(
        String,
        nullable=False,
    )

    estimated_repair_cost = Column(
        Float,
        nullable=False,
    )

    claim_amount = Column(
        Float,
        nullable=False,
    )

    fraud_label = Column(
        String(20),
        nullable=False,
    )

    fraud_score = Column(
        Integer,
        nullable=False,
    )

    claim_status = Column(
        String(30),
        nullable=False,
    )

    inspection_status = Column(
        String(30),
        nullable=False,
    )

    cv_status = Column(
        String(30),
        nullable=False,
    )

    nlp_status = Column(
        String(30),
        nullable=False,
    )

    rag_status = Column(
        String(30),
        nullable=False,
    )

    final_decision = Column(
        String(30),
        nullable=False,
    )

    customer = relationship(
        "Customer",
        back_populates="claims",
    )

    policy = relationship(
        "Policy",
        back_populates="claims",
    )

    ai_detection = relationship(
        "AIDetection",
        back_populates="claim",
        uselist=False,
    )

    nlp_analysis = relationship(
        "NLPAnalysis",
        back_populates="claim",
        uselist=False,
    )

    ai_decision = relationship(
        "AIDecision",
        back_populates="claim",
        uselist=False,
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