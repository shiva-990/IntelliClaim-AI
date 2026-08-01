from pathlib import Path

import cv2
from ultralytics import YOLO

from cv.models.detection import Detection


class DetectorService:

    def __init__(self, model_path: Path):

        self.model = YOLO(str(model_path))

    def detect(self, image):

        results = self.model(image)

        detections = []

        for result in results:

            names = result.names

            for box in result.boxes:

                class_id = int(box.cls[0])

                confidence = float(box.conf[0])

                x1, y1, x2, y2 = box.xyxy[0].tolist()

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