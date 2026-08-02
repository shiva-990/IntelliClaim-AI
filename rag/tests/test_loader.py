from pathlib import Path

from rag.documents.loader import PolicyLoader

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DOCUMENTS = PROJECT_ROOT / "rag" / "documents"

loader = PolicyLoader(DOCUMENTS)

documents = loader.load_documents()

print("=" * 60)

print("Total Pages :", len(documents))

print("=" * 60)

print(documents[0].metadata)

print("=" * 60)

print(documents[0].page_content[:500])