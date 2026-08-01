import os
import random

import pandas as pd

# -----------------------------
# Configuration
# -----------------------------

CUSTOMERS_CSV = "data/customers/customers.csv"
OUTPUT_DIR = "data/vehicles"
OUTPUT_CSV = os.path.join(OUTPUT_DIR, "vehicles.csv")

VEHICLE_MAKES = {
    "Honda": ["City", "Amaze", "Elevate"],
    "Hyundai": ["i20", "Creta", "Venue"],
    "Maruti Suzuki": ["Swift", "Baleno", "Brezza"],
    "Tata": ["Nexon", "Punch", "Harrier"],
    "Mahindra": ["XUV300", "Scorpio", "Thar"],
    "Toyota": ["Innova", "Glanza", "Fortuner"],
    "Kia": ["Seltos", "Sonet", "Carens"],
    "Volkswagen": ["Virtus", "Taigun"],
    "Skoda": ["Slavia", "Kushaq"],
}

STATES = [
    "AP", "TS", "TN", "KA", "MH",
    "DL", "KL", "GJ", "RJ", "UP"
]


def generate_registration():

    state = random.choice(STATES)

    district = random.randint(1, 99)

    letters = "".join(
        random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2)
    )

    number = random.randint(1000, 9999)

    return f"{state}{district:02d}{letters}{number}"


def main():

    customers = pd.read_csv(CUSTOMERS_CSV)

    vehicles = []

    for idx, row in customers.iterrows():

        make = random.choice(list(VEHICLE_MAKES.keys()))

        model = random.choice(VEHICLE_MAKES[make])

        vehicle = {
            "Vehicle_ID": f"VEH{idx+1:05d}",
            "Customer_ID": row["Customer_ID"],
            "Registration_Number": generate_registration(),
            "Make": make,
            "Model": model,
            "Manufacture_Year": random.randint(2017, 2025),
        }

        vehicles.append(vehicle)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    df = pd.DataFrame(vehicles)

    df.to_csv(
        OUTPUT_CSV,
        index=False,
    )

    print("=" * 60)
    print("VEHICLES GENERATED SUCCESSFULLY")
    print("=" * 60)
    print(f"Vehicles : {len(df)}")
    print(f"Saved To : {OUTPUT_CSV}")
    print("=" * 60)

    print("\nSample:\n")
    print(df.head())


if __name__ == "__main__":
    main()