import json
from dataclasses import asdict
from pathlib import Path

from cv.models.prediction import Prediction


class JSONGenerator:

    def generate(
        self,
        prediction: Prediction,
        output_dir: Path,
    ) -> Path:

        output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / (
            Path(prediction.image_name).stem + ".json"
        )

        report = {
            "image_name": prediction.image_name,
            "image_width": prediction.image_width,
            "image_height": prediction.image_height,
            "model_name": prediction.model_name,
            "total_detections": len(prediction.detections),
            "detections": [
                asdict(det) for det in prediction.detections
            ],
        }

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)

        return output_file