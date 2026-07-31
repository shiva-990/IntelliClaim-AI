from rag.retriever.query_embedding import embed_query
from rag.vector_store.pinecone_store import get_pinecone_index


def retrieve_documents(
    query: str,
    policy_number: str = None,
    top_k: int = 5
):
    """
    Retrieve the most relevant chunks from Pinecone.

    If a policy number is provided, search only within that policy.
    Otherwise, perform semantic search across all policies.
    """

    index = get_pinecone_index()

    query_vector = embed_query(query)

    query_kwargs = {
        "vector": query_vector,
        "top_k": top_k,
        "include_metadata": True,
    }

    # Apply metadata filter only if policy number exists
    if policy_number:
        query_kwargs["filter"] = {
            "policy_number": {
                "$eq": policy_number
            }
        }

    results = index.query(**query_kwargs)

    documents = []

    for match in results["matches"]:

        documents.append(
            {
                "score": match["score"],
                "text": match["metadata"]["text"],
                "metadata": match["metadata"],
            }
        )

    return documents