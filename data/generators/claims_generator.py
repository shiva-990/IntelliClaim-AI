import random
from pathlib import Path
from datetime import datetime, timedelta

from damage_rules import (
    generate_claim_amount,
    generate_fraud_label,
    generate_repair_cost,
)

from description_templates import get_description
import pandas as pd
random.seed(42)

# ==========================================================
# CONFIGURATION
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

CUSTOMERS_CSV = PROJECT_ROOT / "data" / "customers" / "customers.csv"
POLICIES_CSV = PROJECT_ROOT / "data" / "policies" / "policy_master.csv"

DATASET_PATH = PROJECT_ROOT / "cv" / "dataset" / "Car_Damage_V5"

TRAIN_IMAGES = DATASET_PATH / "train" / "images"
TRAIN_LABELS = DATASET_PATH / "train" / "labels"

VALID_IMAGES = DATASET_PATH / "valid" / "images"
VALID_LABELS = DATASET_PATH / "valid" / "labels"

TEST_IMAGES = DATASET_PATH / "test" / "images"
TEST_LABELS = DATASET_PATH / "test" / "labels"

# ==========================================================
# OUTPUT FILES
# ==========================================================

CLAIMS_FOLDER = PROJECT_ROOT / "data" / "claims"

VEHICLE_CLAIMS_CSV = CLAIMS_FOLDER / "vehicle_claims.csv"
CLAIM_IMAGES_CSV = CLAIMS_FOLDER / "claim_images.csv"

CLASS_MAP = {
    0: "dent",
    1: "glass_break",
    2: "scratch",
    3: "smash"
}


# ==========================================================
# LOAD CSV FILES
# ==========================================================

def load_customers():
    """Load customer master."""
    customers = pd.read_csv(CUSTOMERS_CSV)
    print(f"Loaded Customers : {len(customers)}")
    return customers


def load_policies():
    """Load policy master."""
    policies = pd.read_csv(POLICIES_CSV)
    print(f"Loaded Policies  : {len(policies)}")
    return policies


# ==========================================================
# READ YOLO LABEL
# ==========================================================

def read_damage_type(label_path: Path):
    """
    Reads a YOLO label file and returns
    the primary damage type.
    """

    if not label_path.exists():
        return None

    with open(label_path, "r") as f:
        lines = f.readlines()

    if len(lines) == 0:
        return None

    class_counts = {}

    for line in lines:

        class_id = int(line.split()[0])

        damage = CLASS_MAP.get(class_id)

        if damage is None:
            continue

        class_counts[damage] = class_counts.get(damage, 0) + 1

    if not class_counts:
        return None

    return max(class_counts, key=class_counts.get)


# ==========================================================
# SCAN DATASET
# ==========================================================

def scan_split(images_folder: Path, labels_folder: Path):
    """
    Scan one dataset split.
    """

    image_records = []

    image_extensions = {".jpg", ".jpeg", ".png"}

    for image_path in sorted(images_folder.iterdir()):

        if image_path.suffix.lower() not in image_extensions:
            continue

        label_path = labels_folder / f"{image_path.stem}.txt"

        damage = read_damage_type(label_path)

        image_records.append(
            {
                "image_name": image_path.name,
                "image_path": str(image_path),
                "label_path": str(label_path),
                "damage_type": damage,
            }
        )

    return image_records


def scan_dataset():
    """
    Scan train + valid + test datasets.
    """

    records = []

    records.extend(scan_split(TRAIN_IMAGES, TRAIN_LABELS))
    records.extend(scan_split(VALID_IMAGES, VALID_LABELS))
    records.extend(scan_split(TEST_IMAGES, TEST_LABELS))

    print(f"\nTotal Images Found : {len(records)}")

    return records

# ==========================================================
# ACTIVE POLICIES
# ==========================================================

def get_active_policies(policies):
    return policies[policies["Policy_Status"] == "Active"]


# ==========================================================
# RANDOM DATES
# ==========================================================

def generate_dates():

    accident_date = datetime.now() - timedelta(
        days=random.randint(1, 180)
    )

    claim_date = accident_date + timedelta(
        days=random.randint(0, 5)
    )

    return (
        accident_date.strftime("%Y-%m-%d"),
        claim_date.strftime("%Y-%m-%d")
    )

# ==========================================================
# CREATE CLAIMS
# ==========================================================

def create_claims(image_records, customers, policies):

    active_policies = get_active_policies(policies)

    vehicle_claims = []
    claim_images = []

    claim_number = 1
    image_index = 0

    while image_index < len(image_records):

        claim_id = f"CLM{claim_number:06d}"

        policy = active_policies.sample(1).iloc[0]

        customer_id = policy["Customer_ID"]
        customer = customers[
        customers["Customer_ID"] == customer_id
        ].iloc[0]

        remaining_images = len(image_records) - image_index

        # Stop if fewer than 2 images remain
        if remaining_images < 2:
            break

        image_count = min(random.randint(2, 4), remaining_images)

        selected_images = image_records[
            image_index:image_index + image_count
    ]

        if not selected_images:
            break

        damage_counts = {}

        for img in selected_images:

            damage = img["damage_type"]

            if damage is None:
                continue

            damage_counts[damage] = damage_counts.get(damage, 0) + 1

        if damage_counts:
           primary_damage = max(
                damage_counts,
                key=damage_counts.get
           )
        else:
            primary_damage = "scratch"

        repair_cost = generate_repair_cost(primary_damage)

        claim_amount = generate_claim_amount(repair_cost)

        fraud = generate_fraud_label(primary_damage)

        # Generate Fraud Score
        if fraud == "Fraud":
            fraud_score = random.randint(70, 100)
        else:
            fraud_score = random.randint(5, 40)

        accident_date, claim_date = generate_dates()

        vehicle_claims.append({

            "Claim_ID": claim_id,

            "Customer_ID": customer["Customer_ID"],

            "Policy_Number": policy["Policy_Number"],

            "Accident_Date": accident_date,

            "Claim_Date": claim_date,

            "Damage_Type": primary_damage,

            "Accident_Description":
                get_description(primary_damage),

            "Estimated_Repair_Cost": repair_cost,

            "Claim_Amount": claim_amount,

            "Fraud_Label": fraud,

            "Fraud_Score": fraud_score,

            "Claim_Status": "Pending",

            "Inspection_Status": "Pending",

            "CV_Status": "Pending",

            "NLP_Status": "Pending",

            "RAG_Status": "Pending",

            "Final_Decision": "Pending"

        })

        positions = [
            "Front",
            "Rear",
            "Left",
            "Right"
        ]
        random.shuffle(positions)
        for idx, img in enumerate(selected_images):

            claim_images.append({

                "Claim_ID": claim_id,

                "Image_Name": img["image_name"],

                "Damage_Type": img["damage_type"],

                "Image_Order": positions[idx]

            })

        claim_number += 1
        image_index += image_count

    return vehicle_claims, claim_images

# ==========================================================
# SAVE CSV FILES
# ==========================================================

def save_claims(vehicle_claims, claim_images):

    CLAIMS_FOLDER.mkdir(parents=True, exist_ok=True)

    vehicle_df = pd.DataFrame(vehicle_claims)
    images_df = pd.DataFrame(claim_images)

    vehicle_df.to_csv(
        VEHICLE_CLAIMS_CSV,
        index=False
    )

    images_df.to_csv(
        CLAIM_IMAGES_CSV,
        index=False
    )

    return vehicle_df, images_df


# ==========================================================
# VALIDATE DATA
# ==========================================================

def validate_data(vehicle_df, images_df):

    print("\n" + "=" * 60)
    print("DATA VALIDATION")
    print("=" * 60)

    # ---------------------------------------
    # Duplicate Claim IDs
    # ---------------------------------------

    duplicate_claims = vehicle_df["Claim_ID"].duplicated().sum()

    print(f"Duplicate Claim IDs            : {duplicate_claims}")

    # ---------------------------------------
    # Missing Customer IDs
    # ---------------------------------------

    missing_customer = vehicle_df["Customer_ID"].isna().sum()

    print(f"Missing Customer IDs           : {missing_customer}")

    # ---------------------------------------
    # Missing Policy Numbers
    # ---------------------------------------

    missing_policy = vehicle_df["Policy_Number"].isna().sum()

    print(f"Missing Policy Numbers         : {missing_policy}")

    # ---------------------------------------
    # Customer-Policy Relationship Validation
    # ---------------------------------------

    policies_df = pd.read_csv(POLICIES_CSV)

    policy_lookup = (
        policies_df
        .set_index("Policy_Number")["Customer_ID"]
        .to_dict()
    )

    relationship_errors = 0

    for _, row in vehicle_df.iterrows():

        expected_customer = policy_lookup.get(
            row["Policy_Number"]
        )

        if expected_customer != row["Customer_ID"]:

            relationship_errors += 1

    print(f"Customer-Policy Mismatches     : {relationship_errors}")

    # ---------------------------------------
    # Image Count Validation
    # ---------------------------------------

    images_per_claim = images_df.groupby(
        "Claim_ID"
    ).size()

    invalid_claims = images_per_claim[
        (images_per_claim < 2) |
        (images_per_claim > 4)
    ]

    print(
        f"Claims with Invalid Image Count: {len(invalid_claims)}"
    )

    # ---------------------------------------
    # Final Status
    # ---------------------------------------

    if (
        duplicate_claims == 0
        and missing_customer == 0
        and missing_policy == 0
        and relationship_errors == 0
        and len(invalid_claims) == 0
    ):
        print("\n✅ DATASET VALIDATION PASSED")

    else:
        print("\n❌ DATASET VALIDATION FAILED")

    print("=" * 60)

# ==========================================================
# PRINT STATISTICS
# ==========================================================

def print_statistics(vehicle_df):

    print("\n" + "=" * 60)
    print("CLAIM STATISTICS")
    print("=" * 60)

    print(f"Total Claims : {len(vehicle_df)}")

    print("\nDamage Distribution")

    print(vehicle_df["Damage_Type"].value_counts())

    print("\nFraud Distribution")

    print(vehicle_df["Fraud_Label"].value_counts())

    print("\nAverage Claim Amount")

    print(f"₹ {vehicle_df['Claim_Amount'].mean():,.2f}")

    print("\nMaximum Claim Amount")

    print(f"₹ {vehicle_df['Claim_Amount'].max():,.2f}")

    print("\nMinimum Claim Amount")

    print(f"₹ {vehicle_df['Claim_Amount'].min():,.2f}")

    print("=" * 60)

# ==========================================================
# MAIN
# ==========================================================

def main():

    print("=" * 60)
    print("INTELLICLAIM AI - CLAIMS GENERATOR (PART 2)")
    print("=" * 60)

    # ----------------------------------------
    # Load Master Data
    # ----------------------------------------

    customers = load_customers()
    policies = load_policies()

    # ----------------------------------------
    # Scan YOLO Dataset
    # ----------------------------------------

    image_records = scan_dataset()

    # ----------------------------------------
    # Generate Claims
    # ----------------------------------------

    vehicle_claims, claim_images = create_claims(
        image_records=image_records,
        customers=customers,
        policies=policies
    )
    # ----------------------------------------
    # Save CSV Files
    # ----------------------------------------

    vehicle_df, images_df = save_claims(
        vehicle_claims,
        claim_images
    )

    # ----------------------------------------
    # Validate Generated Data
    # ----------------------------------------

    validate_data(
        vehicle_df,
        images_df
    )

    # ----------------------------------------
    # Print Statistics
    # ----------------------------------------

    print_statistics(
        vehicle_df
    )
    # ----------------------------------------
    # Summary
    # ----------------------------------------

    print("\n" + "=" * 60)
    print("CLAIM GENERATION SUMMARY")
    print("=" * 60)

    print(f"Customers Loaded      : {len(customers)}")
    print(f"Policies Loaded       : {len(policies)}")
    print(f"Images Scanned        : {len(image_records)}")
    print(f"Claims Generated      : {len(vehicle_claims)}")
    print(f"Claim Images Created  : {len(claim_images)}")

    # ----------------------------------------
    # Sample Claim
    # ----------------------------------------

    print("\nSample Claim")
    print("-" * 60)

    if vehicle_claims:
        for key, value in vehicle_claims[0].items():
            print(f"{key:25}: {value}")

    # ----------------------------------------
    # Sample Image Records
    # ----------------------------------------

    print("\nSample Claim Images")
    print("-" * 60)

    for row in claim_images[:5]:
        print(row)

    print("\n" + "=" * 60)
    print("PART 2 COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()