import pandas as pd

from database.connection import SessionLocal

from database.models.claim import Claim
from database.models.customer import Customer
from database.models.policy import Policy
from database.models.vehicle import Vehicle

CSV_PATH = "data/claims/vehicle_claims.csv"


def seed_claims():

    db = SessionLocal()

    df = pd.read_csv(CSV_PATH)

    inserted = 0
    skipped = 0

    print("=" * 60)
    print("SEEDING CLAIMS")
    print("=" * 60)

    for _, row in df.iterrows():

        # ----------------------------
        # Duplicate Check
        # ----------------------------
        existing = (
            db.query(Claim)
            .filter(
                Claim.claim_id == row["Claim_ID"]
            )
            .first()
        )

        if existing:
            skipped += 1
            continue

        # ----------------------------
        # Customer Validation
        # ----------------------------
        customer = (
            db.query(Customer)
            .filter(
                Customer.customer_id == row["Customer_ID"]
            )
            .first()
        )

        if customer is None:
            print(f"Customer Not Found : {row['Customer_ID']}")
            skipped += 1
            continue

        # ----------------------------
        # Policy Validation
        # ----------------------------
        policy = (
            db.query(Policy)
            .filter(
                Policy.policy_number == row["Policy_Number"]
            )
            .first()
        )

        if policy is None:
            print(f"Policy Not Found : {row['Policy_Number']}")
            skipped += 1
            continue

        # ----------------------------
        # Vehicle Validation
        # ----------------------------
        vehicle = (
            db.query(Vehicle)
            .filter(
                Vehicle.customer_id == row["Customer_ID"]
            )
            .first()
        )

        if vehicle is None:
            print(f"Vehicle Not Found for Customer : {row['Customer_ID']}")
            skipped += 1
            continue

        # ----------------------------
        # Insert Claim
        # ----------------------------
        claim = Claim(

            claim_id=row["Claim_ID"],

            customer_id=row["Customer_ID"],

            policy_number=row["Policy_Number"],

            accident_date=pd.to_datetime(
                row["Accident_Date"]
            ).date(),

            claim_date=pd.to_datetime(
                row["Claim_Date"]
            ).date(),

            damage_type=row["Damage_Type"],

            accident_description=row[
                "Accident_Description"
            ],

            estimated_repair_cost=float(
                row["Estimated_Repair_Cost"]
            ),

            claim_amount=float(
                row["Claim_Amount"]
            ),

            fraud_label=row["Fraud_Label"],

            fraud_score=int(
                row["Fraud_Score"]
            ),

            claim_status=row["Claim_Status"],

            inspection_status=row["Inspection_Status"],

            cv_status=row["CV_Status"],

            nlp_status=row["NLP_Status"],

            rag_status=row["RAG_Status"],

            final_decision=row["Final_Decision"],
        )

        db.add(claim)

        inserted += 1

    db.commit()

    db.close()

    print("=" * 60)
    print("CLAIMS SEEDED")
    print("=" * 60)
    print(f"Inserted : {inserted}")
    print(f"Skipped  : {skipped}")
    print("=" * 60)


if __name__ == "__main__":
    seed_claims()