from rag.embeddings.embedding_model import get_embedding_model


def embed_query(query: str):
    """
    Generate embedding for a user query.
    """

    embedding_model = get_embedding_model()

    return embedding_model.embed_query(query)