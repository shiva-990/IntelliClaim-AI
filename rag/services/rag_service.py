from database.crud.claim import get_claim

from rag.retriever.retriever import PolicyRetriever
from rag.llm.answer_generator import AnswerGenerator


class RAGService:

    def __init__(self):

        self.retriever = PolicyRetriever()

        self.generator = AnswerGenerator()

    def verify_policy(
        self,
        db,
        claim_id: str,
    ):

        claim = get_claim(
            db,
            claim_id,
        )

        if claim is None:
            raise Exception(
                "Claim not found."
            )

        question = (
            f"""
            Policy Number: {claim.policy_number}

            Claim Description:
            {claim.accident_description}

            Is this claim covered?

            If yes explain why.

            If no explain why.

            Mention deductible if available.
            """
        )

        documents = self.retriever.search(
            question
        )

        answer = self.generator.answer(
            question,
            documents,
        )

        return answer