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

        # -------------------------------------------------
        # Fetch Claim
        # -------------------------------------------------

        claim = get_claim(
            db,
            claim_id,
        )

        if claim is None:
            raise Exception(
                "Claim not found."
            )

        # -------------------------------------------------
        # Build Question for LLM
        # -------------------------------------------------

        question = f"""
Policy Number:
{claim.policy_number}

Claim Description:
{claim.accident_description}

Is this claim covered?

If yes, explain why.

If no, explain why.

Mention deductible if available.
"""

        # -------------------------------------------------
        # Retrieve Documents from FAISS
        # -------------------------------------------------

        documents = self.retriever.search(
            claim.policy_number,
            k=5,
        )

        # -------------------------------------------------
        # Debug Retrieved Documents
        # -------------------------------------------------

        print("\n" + "=" * 80)
        print("RAG RETRIEVED DOCUMENTS")
        print("=" * 80)

        if not documents:
            print("No documents retrieved from FAISS.")

        for index, doc in enumerate(documents, start=1):

            print(f"\nDocument {index}")
            print("-" * 80)

            if hasattr(doc, "metadata"):
                print("Metadata:")
                print(doc.metadata)

            print("\nContent:")
            print(doc.page_content[:1000])

            print("-" * 80)

        print("=" * 80 + "\n")

        # -------------------------------------------------
        # Generate Answer
        # -------------------------------------------------

        answer = self.generator.answer(
            question,
            documents,
        )

        print("\n" + "=" * 80)
        print("RAG FINAL ANSWER")
        print("=" * 80)
        print(answer)
        print("=" * 80 + "\n")

        return answer