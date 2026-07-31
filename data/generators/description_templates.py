import random

ACCIDENT_DESCRIPTIONS = {

    "scratch": [

        "Vehicle was scratched while parking in a shopping mall.",

        "Driver accidentally brushed the vehicle against a concrete wall while reversing.",

        "Minor scratches occurred due to contact with another parked vehicle.",

        "Side panel was scratched while passing through a narrow street.",

        "Scratches were noticed after the vehicle was parked overnight."

    ],

    "dent": [

        "Vehicle suffered a dent after a rear-end collision.",

        "Driver hit a roadside pole while taking a turn.",

        "A low-speed collision caused dents on the front bumper.",

        "Another vehicle hit the car while waiting at a traffic signal.",

        "Vehicle was dented after accidental impact with a divider."

    ],

    "glass_break": [

        "Windshield cracked after being struck by flying debris.",

        "A stone from a truck shattered the front windshield.",

        "Side window broke after impact from roadside debris.",

        "Windshield developed cracks following a highway incident.",

        "Glass damage occurred due to falling construction material."

    ],

    "smash": [

        "Major highway collision caused extensive front-end damage.",

        "Vehicle collided with a divider resulting in severe body damage.",

        "A high-speed accident caused significant structural damage.",

        "Vehicle was heavily damaged after colliding with another car.",

        "Front portion of the vehicle was severely smashed during an accident."

    ]

}

def get_description(damage_type):
    return random.choice(
        ACCIDENT_DESCRIPTIONS.get(
            damage_type,
            ["Accident description unavailable."]
        )
    )