from functools import lru_cache
from langchain_huggingface import HuggingFaceEmbeddings


@lru_cache(maxsize=1)
def get_embedding_model():
    """
    Load the embedding model only once and reuse it.
    """

    print("=" * 60)
    print("LOADING EMBEDDING MODEL")
    print("=" * 60)
    print("Model : BAAI/bge-small-en-v1.5")

    embedding_model = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )

    print("Embedding model loaded successfully.")

    return embedding_model