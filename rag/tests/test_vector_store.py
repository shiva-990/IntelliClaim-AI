from pathlib import Path

from rag.documents.loader import PolicyLoader
from rag.documents.splitter import PolicySplitter
from rag.vector_store.faiss_store import FAISSStore

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DOCUMENTS = PROJECT_ROOT / "rag" / "documents"

VECTOR_DB = PROJECT_ROOT / "rag" / "vector_db"

VECTOR_DB.mkdir(
    exist_ok=True,
)

loader = PolicyLoader(DOCUMENTS)

documents = loader.load_documents()

splitter = PolicySplitter()

chunks = splitter.split(documents)

store = FAISSStore()

db = store.create(chunks)

store.save(
    db,
    VECTOR_DB,
)

print("=" * 60)
print("Vector DB Created")
print("=" * 60)
print("Chunks :", len(chunks))
print("Saved :", VECTOR_DB)