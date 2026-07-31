import cv2
from pathlib import Path
from typing import List

from cv.models.detection import Detection


class Visualizer:

    def draw(
        self,
        image,
        detections: List[Detection],
        output_path: Path,
    ) -> Path:

        annotated = image.copy()

        for detection in detections:

            x1, y1, x2, y2 = map(int, detection.bbox)

            cv2.rectangle(
                annotated,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2,
            )

            label = (
                f"{detection.class_name} | "
                f"{detection.confidence:.2f} | "
                f"{detection.severity}"
            )

            cv2.putText(
                annotated,
                label,
                (x1, max(30, y1 - 10)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2,
            )

        output_path.parent.mkdir(parents=True, exist_ok=True)

        cv2.imwrite(str(output_path), annotated)

        return output_path