class ClaimInformationExtractor:

    ACCIDENT_PATTERNS = {
        "Rear Collision": [
            "rear",
            "behind",
            "from behind",
            "rear ended",
        ],

        "Front Collision": [ 
            "front",
            "head on",
            "head-on",
        ],

        "Side Collision": [
            "side",
            "left side",
            "right side",
        ],

        "Fire Damage": [
            "fire",
            "burn",
            "burnt",
        ],

        "Rollover": [
            "rollover",
            "rolled over",
            "overturned",
        ],
    }

    WEATHER = [
        "rain",
        "fog",
        "snow",
        "storm",
        "sunny",
    ]

    VEHICLE_PARTS = [
        "front",
        "rear",
        "door",
        "bumper",
        "hood",
        "bonnet",
        "windshield",
        "light",
        "fender",
    ]

    @classmethod
    def extract(cls, text):

        info = {
            "accident_type": None,
            "vehicle_part": None,
            "weather": None,
        }

        for accident_type, keywords in cls.ACCIDENT_PATTERNS.items():

            if any(keyword in text for keyword in keywords):
                info["accident_type"] = accident_type
                break

        for part in cls.VEHICLE_PARTS:

            if part in text:
                info["vehicle_part"] = part
                break

        for weather in cls.WEATHER:

            if weather in text:
                info["weather"] = weather
                break

        return info 