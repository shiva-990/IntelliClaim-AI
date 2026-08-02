from pathlib import Path

from rag.documents.loader import PolicyLoader
from rag.documents.splitter import PolicySplitter

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DOCUMENTS = PROJECT_ROOT / "rag" / "documents"

loader = PolicyLoader(DOCUMENTS)

documents = loader.load_documents()

splitter = PolicySplitter()

chunks = splitter.split(documents)

print("=" * 60)
print("Total Chunks :", len(chunks))
print("=" * 60)

print(chunks[0].metadata)

print("=" * 60)

print(chunks[0].page_content)