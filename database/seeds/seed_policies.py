import pandas as pd

from database.connection import SessionLocal
from database.models.policy import Policy

CSV_PATH = "data/policies/policy_master.csv"


def seed_policies():

    db = SessionLocal()

    df = pd.read_csv(CSV_PATH)

    inserted = 0
    skipped = 0

    for _, row in df.iterrows():

        existing = (
            db.query(Policy)
            .filter(
                Policy.policy_number == row["Policy_Number"]
            )
            .first()
        )

        if existing:
            skipped += 1
            continue

        policy = Policy(
            policy_number=row["Policy_Number"],
            customer_id=row["Customer_ID"],
            policy_type=row["Policy_Type"],
            insurance_provider=row["Insurance_Provider"],
            premium_amount=row["Premium_Amount"],
            sum_insured=row["Sum_Insured"],
            deductible=row["Deductible"],
            roadside_assistance=row["Roadside_Assistance"],
            engine_protection=row["Engine_Protection"],
            personal_accident_cover=row["Personal_Accident_Cover"],
            valid_from=pd.to_datetime(row["Valid_From"]).date(),
            valid_to=pd.to_datetime(row["Valid_To"]).date(),
            policy_status=row["Policy_Status"],
        )

        db.add(policy)
        inserted += 1

    db.commit()
    db.close()

    print("=" * 60)
    print("POLICIES SEEDED")
    print("=" * 60)
    print(f"Inserted : {inserted}")
    print(f"Skipped  : {skipped}")
    print("=" * 60)


if __name__ == "__main__":
    seed_policies()