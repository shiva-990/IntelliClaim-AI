import pandas as pd

from database.connection import SessionLocal
from database.models.customer import Customer


CSV_PATH = "data/customers/customers.csv"


def seed_customers():

    db = SessionLocal()

    df = pd.read_csv(CSV_PATH)

    inserted = 0
    skipped = 0

    for _, row in df.iterrows():

        existing = (
            db.query(Customer)
            .filter(
                Customer.customer_id == row["Customer_ID"]
            )
            .first()
        )

        if existing:
            skipped += 1
            continue

        customer = Customer(
            customer_id=row["Customer_ID"],
            customer_name=row["Customer_Name"],
            age=row["Age"],
            gender=row["Gender"],
            phone=row["Phone"],
            email=row["Email"],
            address=row["Address"],
            city=row["City"],
            state=row["State"],
            pincode=str(row["Pincode"]),
            driving_license_no=row["Driving_License_No"],
        )

        db.add(customer)
        inserted += 1

    db.commit()

    db.close()

    print("=" * 60)
    print("CUSTOMERS SEEDED")
    print("=" * 60)
    print(f"Inserted : {inserted}")
    print(f"Skipped  : {skipped}")
    print("=" * 60)


if __name__ == "__main__":
    seed_customers()