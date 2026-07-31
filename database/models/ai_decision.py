from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database.base import Base


class AIDecision(Base):
    __tablename__ = "ai_decisions"

    decision_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    claim_id = Column(
        String(20),
        ForeignKey("claims.claim_id"),
        unique=True
    )

    coverage = Column(String(20))

    fraud_score = Column(Float)

    decision = Column(String(50))

    reason = Column(String)

    claim = relationship(
        "Claim",
        back_populates="ai_decision"
    )