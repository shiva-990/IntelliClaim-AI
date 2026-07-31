import random

DAMAGE_RULES = {
    "scratch": {
        "repair_cost": (3000, 15000),
        "fraud_probability": 0.03
    },
    "dent": {
        "repair_cost": (8000, 35000),
        "fraud_probability": 0.08
    },
    "glass_break": {
        "repair_cost": (12000, 45000),
        "fraud_probability": 0.10
    },
    "smash": {
        "repair_cost": (50000, 180000),
        "fraud_probability": 0.18
    }
}


def generate_repair_cost(damage_type):
    low, high = DAMAGE_RULES[damage_type]["repair_cost"]
    return random.randint(low, high)


def generate_claim_amount(repair_cost):
    deductible = random.choice([1000, 2000, 3000, 5000])
    return max(repair_cost - deductible, 1000)


def generate_fraud_label(damage_type):
    probability = DAMAGE_RULES[damage_type]["fraud_probability"]

    if random.random() < probability:
        return "Fraud"

    return "Genuine"