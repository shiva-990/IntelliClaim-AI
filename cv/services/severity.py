from typing import List

from cv.models.detection import Detection


class SeverityEngine:
    """
    Calculates damage severity based on bounding-box size.
    """

    def calculate(
        self,
        detections: List[Detection],
        image_width: int,
        image_height: int,
    ) -> List[Detection]:

        image_area = image_width * image_height

        for detection in detections:

            x1, y1, x2, y2 = detection.bbox

            bbox_area = (x2 - x1) * (y2 - y1)

            area_percent = (bbox_area / image_area) * 100

            detection.damage_area_percent = round(area_percent, 2)

            if area_percent < 5:
                detection.severity = "Minor"

            elif area_percent < 15:
                detection.severity = "Moderate"

            else:
                detection.severity = "Severe"

        return detections