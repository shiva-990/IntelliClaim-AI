from database.connection import SessionLocal

from rag.services.rag_service import RAGService

db = SessionLocal()

service = RAGService()

answer = service.verify_policy(
    db,
    "CLM000001",
)

print("=" * 60)

print(answer)

print("=" * 60)

db.close()