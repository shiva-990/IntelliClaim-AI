from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database.base import Base


class NLPAnalysis(Base):

    __tablename__ = "nlp_analysis"

    id = Column(Integer, primary_key=True, index=True)

    claim_id = Column(
       String(20),
       ForeignKey("claims.claim_id"),
       nullable=False,
    )

    accident_type = Column(String)

    vehicle_part = Column(String)

    weather = Column(String)

    severity = Column(String)

    cause = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    ) 
    claim = relationship(
        "Claim",
         back_populates="nlp_analysis",
    )
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    claim = relationship(
        "Claim",
        back_populates="nlp_analysis",
    )