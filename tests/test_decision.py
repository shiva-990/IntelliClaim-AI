from database.connection import SessionLocal

from services.decision_service import DecisionService


db = SessionLocal()

service = DecisionService()

decision = service.process_claim(
    db,
    "CLM000001",
)

print("=" * 60)

print("Decision ID :", decision.decision_id)
print("Claim ID    :", decision.claim_id)
print("Coverage    :", decision.coverage)
print("Fraud Score :", decision.fraud_score)
print("Decision    :", decision.decision)
print("Reason      :", decision.reason)

print("=" * 60)

db.close()