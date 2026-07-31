from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Detection:
    class_id: int
    class_name: str
    confidence: float
    bbox: List[float]

    severity: Optional[str] = None
    damage_area_percent: Optional[float] = None

    def to_dict(self):
        return {
            "class_id": self.class_id,
            "class_name": self.class_name,
            "confidence": self.confidence,
            "bbox": self.bbox,
            "severity": self.severity,
            "damage_area_percent": self.damage_area_percent,
        }