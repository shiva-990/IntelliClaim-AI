from pathlib import Path

# ==========================================================
# PROJECT PATHS
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"

POLICY_PDF_DIR = DATA_DIR / "policies" / "pdfs"

VECTOR_DB_DIR = PROJECT_ROOT / "vector_db"

VECTOR_DB_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================================
# DOCUMENT SETTINGS
# ==========================================================

CHUNK_SIZE = 800

CHUNK_OVERLAP = 150

# ==========================================================
# EMBEDDING MODEL
# ==========================================================

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

# ==========================================================
# PINECONE
# ==========================================================

PINECONE_INDEX = "intelliclaim-policy-index"