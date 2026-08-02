from pathlib import Path

from rag.vector_store.faiss_store import FAISSStore


class PolicyRetriever:

    def __init__(self):

        PROJECT_ROOT = Path(__file__).resolve().parents[2]

        VECTOR_DB = PROJECT_ROOT / "rag" / "vector_db"

        self.db = FAISSStore().load(VECTOR_DB)

    def search(
        self,
        query: str,
        k: int = 3,
    ):

        return self.db.similarity_search(
            query,
            k=k,
        )