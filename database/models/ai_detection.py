from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    ForeignKey,
    DateTime,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database.base import Base


class AIDetection(Base):

    __tablename__ = "ai_detections"

    id = Column(Integer, primary_key=True, index=True)

    claim_id = Column(
        String(20),
        ForeignKey("claims.claim_id"),
        nullable=False,
    )

    image_name = Column(String, nullable=False)

    detections = Column(JSONB, nullable=False)

    severity = Column(String)

    repair_cost = Column(Float)

    repair_days = Column(Integer)

    repairable = Column(Boolean)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    claim = relationship(
        "Claim",
         back_populates="ai_detection",
    )
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    claim = relationship(
        "Claim",
        back_populates="ai_detection",
    )
