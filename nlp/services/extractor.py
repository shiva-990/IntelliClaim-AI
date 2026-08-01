import spacy

from nlp.models.analysis import Analysis


class Extractor:

    def __init__(self):

        self.nlp = spacy.load("en_core_web_sm")

    def extract(self, text: str):

        doc = self.nlp(text.lower())

        accident_type = "Unknown"
        vehicle_part = "Unknown"
        weather = "Unknown"
        severity = "Low"
        cause = "Unknown"

        # -----------------------------
        # Accident Type
        # -----------------------------
        if "rear" in text.lower():
            accident_type = "Rear Collision"

        elif "front" in text.lower():
            accident_type = "Front Collision"

        elif "side" in text.lower():
            accident_type = "Side Collision"

        elif "rollover" in text.lower():
            accident_type = "Rollover"

        # -----------------------------
        # Vehicle Part
        # -----------------------------
        parts = [
            "bumper",
            "door",
            "bonnet",
            "hood",
            "fender",
            "windshield",
            "light",
            "mirror",
            "roof",
        ]

        for part in parts:

            if part in text.lower():

                vehicle_part = part.title()

                break

        # -----------------------------
        # Weather
        # -----------------------------
        if "rain" in text.lower():

            weather = "Rain"

        elif "fog" in text.lower():

            weather = "Fog"

        elif "snow" in text.lower():

            weather = "Snow"

        elif "sunny" in text.lower():

            weather = "Sunny"

        # -----------------------------
        # Severity
        # -----------------------------
        if any(
            word in text.lower()
            for word in [
                "total",
                "severe",
                "major",
                "destroyed",
            ]
        ):

            severity = "High"

        elif any(
            word in text.lower()
            for word in [
                "medium",
                "moderate",
            ]
        ):

            severity = "Medium"

        # -----------------------------
        # Cause
        # -----------------------------
        if "truck" in text.lower():

            cause = "Truck Collision"

        elif "bike" in text.lower():

            cause = "Bike Collision"

        elif "car" in text.lower():

            cause = "Car Collision"

        return Analysis(

            accident_type=accident_type,

            vehicle_part=vehicle_part,

            weather=weather,

            severity=severity,

            cause=cause,
        )