import pandas as pd

from database.connection import SessionLocal
from database.models.vehicle import Vehicle

CSV_PATH = "data/vehicles/vehicles.csv"


def seed_vehicles():

    db = SessionLocal()

    df = pd.read_csv(CSV_PATH)

    inserted = 0
    skipped = 0

    for _, row in df.iterrows():

        vehicle_id = int(str(row["Vehicle_ID"]).replace("VEH", ""))

        existing = (
            db.query(Vehicle)
            .filter(
                Vehicle.vehicle_id == vehicle_id
             )
            .first()
   ) 

        if existing:
            skipped += 1
            continue

    vehicle = Vehicle(
        vehicle_id=vehicle_id,
        customer_id=row["Customer_ID"],
        registration_number=row["Registration_Number"],
        make=row["Make"],
        model=row["Model"],
        manufacture_year=int(row["Manufacture_Year"]),
    )

    db.add(vehicle)
    inserted += 1

    db.commit()
    db.close()

    print("=" * 60)
    print("VEHICLES SEEDED")
    print("=" * 60)
    print(f"Inserted : {inserted}")
    print(f"Skipped  : {skipped}")
    print("=" * 60)


if __name__ == "__main__":
    seed_vehicles()