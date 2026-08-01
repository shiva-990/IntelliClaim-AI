from sqlalchemy.orm import Session

from nlp.models.preprocess import TextPreprocessor
from nlp.models.extractor import ClaimInformationExtractor
from nlp.models.classifier import ClaimClassifier

from database.schemas.nlp_analysis import NLPAnalysisCreate
from database.crud.nlp_analysis import create_nlp_analysis


class NLPService:

    @classmethod
    def analyze_claim(
        cls,
        db: Session,
        claim_id: int,
        text: str,
    ):

        cleaned = TextPreprocessor.clean(text)

        extracted = ClaimInformationExtractor.extract(cleaned)

        classified = ClaimClassifier.classify(cleaned)

        final_result = {
            **extracted,
            **classified,
        }

        create_nlp_analysis(
            db,
            NLPAnalysisCreate(
                claim_id=claim_id,
                **final_result,
            ),
        )

        return final_result