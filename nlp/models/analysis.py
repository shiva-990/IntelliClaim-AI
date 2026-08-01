from dataclasses import dataclass


@dataclass
class Analysis:

    accident_type: str

    vehicle_part: str

    weather: str

    severity: str

    cause: str