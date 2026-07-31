from pathlib import Path
from typing import List, Dict
from cv.models.detection import Detection
from ultralytics import YOLO
import numpy as np


class DetectorService:
    """
    YOLO Damage Detection Service.
    """

    def __init__(self, model_path: Path):

        if not model_path.exists():
            raise FileNotFoundError(f"Model not found: {model_path}")

        self.model = YOLO(str(model_path))

    def detect(self, image: np.ndarray) -> List[Dict]:
        """
        Run inference on an image.

        Returns:
            List of detections.
        """

        results = self.model(image, verbose=False)

        detections = []

        result = results[0]

        names = result.names

        for box in result.boxes:

            x1, y1, x2, y2 = map(float, box.xyxy[0])

            class_id = int(box.cls[0])

            confidence = float(box.conf[0])

            detections.append(
               Detection(
                  class_id=class_id,
                  class_name=names[class_id],
                  confidence=round(confidence, 4),
                  bbox=[
                      round(x1, 2),
                      round(y1, 2),
                      round(x2, 2),
                      round(y2, 2),
                ],
            )
        )

        return detections