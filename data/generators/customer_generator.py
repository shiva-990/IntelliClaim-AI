from faker import Faker
import pandas as pd
import random
import os

# Initialize Faker for Indian data
fake = Faker("en_IN")

# Number of customers
NUM_CUSTOMERS = 100

customers = []

for i in range(1, NUM_CUSTOMERS + 1):

    customer = {
        "Customer_ID": f"CUST{i:05d}",
        "Customer_Name": fake.name(),
        "Age": random.randint(21, 70),
        "Gender": random.choice(["Male", "Female"]),
        "Phone": fake.phone_number(),
        "Email": fake.email(),
        "Address": fake.address().replace("\n", ", "),
        "City": fake.city(),
        "State": fake.state(),
        "Pincode": fake.postcode(),
        "Driving_License_No": fake.bothify(text="??## ##########").upper()
    }

    customers.append(customer)

df = pd.DataFrame(customers)

output_dir = "data/customers"
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "customers.csv")

df.to_csv(output_path, index=False)

print("=" * 60)
print("Customer Master Generated Successfully!")
print(f"Total Customers : {len(df)}")
print(f"Saved To         : {output_path}")
print("=" * 60)

print("\nSample Data:\n")
print(df.head())