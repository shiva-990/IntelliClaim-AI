from typing import List


class DamageAnalysisService:

    DAMAGE_RULES = {
        "scratch": {
            "severity": "Low",
            "cost": 5000,
            "days": 2,
        },
        "dent": {
            "severity": "Medium",
            "cost": 15000,
            "days": 4,
        },
        "crack": {
            "severity": "Medium",
            "cost": 18000,
            "days": 5,
        },
        "smash": {
            "severity": "High",
            "cost": 30000,
            "days": 7,
        },
    }

    @classmethod
    def analyze(cls, detections: List[dict]):

        if not detections:
            return {
                "severity": "No Damage",
                "repair_cost": 0,
                "repair_days": 0,
                "repairable": True,
            }

        highest_cost = 0
        final = None

        for detection in detections:

            part = detection["part"]

            if part not in cls.DAMAGE_RULES:
                continue

            rule = cls.DAMAGE_RULES[part]

            if rule["cost"] > highest_cost:
                highest_cost = rule["cost"]
                final = rule

        return {
            "severity": final["severity"],
            "repair_cost": final["cost"],
            "repair_days": final["days"],
            "repairable": final["cost"] < 80000,
        }