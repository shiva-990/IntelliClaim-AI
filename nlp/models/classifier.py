class ClaimClassifier:

    HIGH_SEVERITY = [
        "rollover",
        "fire",
        "explosion",
        "truck",
        "fatal",
    ]

    MEDIUM_SEVERITY = [
        "rear",
        "side",
        "collision",
        "crash",
        "bike",
    ]

    LOW_SEVERITY = [
        "scratch",
        "minor",
        "parking",
        "dent",
    ]

    @classmethod
    def classify(cls, text):

        text = text.lower()

        severity = "Low"

        for word in cls.HIGH_SEVERITY:
            if word in text:
                severity = "High"
                break

        if severity == "Low":
            for word in cls.MEDIUM_SEVERITY:
                if word in text:
                    severity = "Medium"
                    break

        cause = "Unknown"

        if "bike" in text:
            cause = "Bike"

        elif "car" in text:
            cause = "Car"

        elif "truck" in text:
            cause = "Truck"

        elif "tree" in text:
            cause = "Tree"

        elif "pole" in text:
            cause = "Pole"

        return {
            "severity": severity,
            "cause": cause,
        } 