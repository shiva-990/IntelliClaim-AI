from pathlib import Path

from langchain_community.vectorstores import FAISS

from rag.embeddings.embedding_model import EmbeddingModel


class FAISSStore:

    def __init__(self):

        self.embedding = EmbeddingModel().get_model()

    def create(self, chunks):

        return FAISS.from_documents(
            chunks,
            self.embedding,
        )

    def save(
        self,
        db,
        save_path: Path,
    ):

        db.save_local(str(save_path))

    def load(
        self,
        save_path: Path,
    ):

        return FAISS.load_local(
            str(save_path),
            self.embedding,
            allow_dangerous_deserialization=True,
        )