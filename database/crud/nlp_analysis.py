from sqlalchemy.orm import Session

from database.models.nlp_analysis import NLPAnalysis
from database.schemas.nlp_analysis import NLPAnalysisCreate


def create_nlp_analysis(
    db: Session,
    analysis: NLPAnalysisCreate,
):

    db_analysis = NLPAnalysis(**analysis.model_dump())

    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)

    return db_analysis


def get_nlp_analysis(
    db: Session,
    claim_id: int,
):

    return (
        db.query(NLPAnalysis)
        .filter(
            NLPAnalysis.claim_id == claim_id
        )
        .first()
    ) 
def get_nlp_analysis(
    db: Session,
    claim_id: str,
):

    return (
        db.query(NLPAnalysis)
        .filter(
            NLPAnalysis.claim_id == claim_id
        )
        .first()
    )