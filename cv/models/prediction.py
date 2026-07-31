from dataclasses import dataclass, field
from typing import List

from cv.models.detection import Detection


@dataclass
class Prediction:
    image_name: str
    image_width: int
    image_height: int
    model_name: str

    detections: List[Detection] = field(default_factory=list)