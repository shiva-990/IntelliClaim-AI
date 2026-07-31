from rag.retriever.pinecone_retriever import retrieve_documents
from rag.llm.answer_generator import generate_answer
from rag.utils.policy_parser import extract_policy_number


def ask_question(question: str):
    """
    Complete IntelliClaim RAG Pipeline

    1. Extract Policy Number (if present)
    2. Retrieve relevant policy chunks
    3. Generate answer using Qwen
    """

    # -------------------------------------------------
    # Extract Policy Number
    # -------------------------------------------------

    policy_number = extract_policy_number(question)

    if policy_number:
        print(f"\nPolicy Detected : {policy_number}")
    else:
        print("\nNo Policy Number Detected")

    # -------------------------------------------------
    # Retrieve Documents
    # -------------------------------------------------

    retrieved_docs = retrieve_documents(
        query=question,
        policy_number=policy_number,
        top_k=5,
    )

    if not retrieved_docs:
        return "No relevant policy information found."

    # -------------------------------------------------
    # Display Retrieved Documents (Debug)
    # -------------------------------------------------

    print("\n" + "=" * 70)
    print("RETRIEVED DOCUMENTS")
    print("=" * 70)

    context_parts = []

    for i, doc in enumerate(retrieved_docs, start=1):

        print(f"\nDocument {i}")
        print(f"Score : {doc['score']:.4f}")

        metadata = doc["metadata"]

        print(f"Policy : {metadata.get('policy_number', 'N/A')}")
        print(f"Page   : {metadata.get('page', 'N/A')}")

        print("-" * 60)

        preview = doc["text"][:250].replace("\n", " ")

        print(preview + "...")

        context_parts.append(doc["text"])

    # -------------------------------------------------
    # Build Context
    # -------------------------------------------------

    context = "\n\n".join(context_parts)

    # -------------------------------------------------
    # Generate Final Answer
    # -------------------------------------------------

    answer = generate_answer(
        context=context,
        question=question
    )

    return answer