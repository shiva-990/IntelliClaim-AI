import pandas as pd
import random
import os
from faker import Faker
from datetime import timedelta

fake = Faker("en_IN")

# -----------------------------
# Configuration
# -----------------------------
NUM_POLICIES = 30

INSURANCE_PROVIDERS = [
    "Digit Insurance",
    "ICICI Lombard",
    "HDFC ERGO",
    "Tata AIG",
    "Bajaj Allianz",
    "ACKO",
    "Reliance General",
    "SBI General",
    "New India Assurance",
    "Oriental Insurance"
]

POLICY_TYPES = [
    "Comprehensive",
    "Third Party",
    "Zero Depreciation"
]

SUM_INSURED_OPTIONS = [
    500000,
    700000,
    800000,
    1000000,
    1200000,
    1500000
]

policies = []

for i in range(1, NUM_POLICIES + 1):

    valid_from = fake.date_between(start_date="-2y", end_date="today")
    valid_to = valid_from + timedelta(days=365)

    sum_insured = random.choice(SUM_INSURED_OPTIONS)

    premium = round(sum_insured * random.uniform(0.018, 0.04))

    deductible = random.choice([1000, 2000, 3000, 5000])

    policy = {
        "Policy_Number": f"POL{i:05d}",
        "Policy_Type": random.choice(POLICY_TYPES),
        "Insurance_Provider": random.choice(INSURANCE_PROVIDERS),
        "Premium_Amount": premium,
        "Sum_Insured": sum_insured,
        "Deductible": deductible,
        "Roadside_Assistance": random.choice(["Yes", "No"]),
        "Engine_Protection": random.choice(["Yes", "No"]),
        "Personal_Accident_Cover": random.choice(["Yes", "No"]),
        "Valid_From": valid_from,
        "Valid_To": valid_to,
        "Policy_Status": random.choice(["Active", "Expired"])
    }

    policies.append(policy)

df = pd.DataFrame(policies)

output_dir = "data/policies"
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "policy_master.csv")

df.to_csv(output_path, index=False)

print("=" * 60)
print("Policy Master Generated Successfully!")
print(f"Total Policies : {len(df)}")
print(f"Saved To       : {output_path}")
print("=" * 60)

print("\nSample Policies:\n")
print(df.head())