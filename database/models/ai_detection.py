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

from database.base import Base


class AIDetection(Base):

    __tablename__ = "ai_detections"

    id = Column(Integer, primary_key=True, index=True)

    claim_id = Column(
        Integer,
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