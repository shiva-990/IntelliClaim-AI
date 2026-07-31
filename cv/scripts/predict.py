from pathlib import Path

from configs.settings import (
    MODEL_PATH,
    JSON_OUTPUT_DIR,
    IMAGE_OUTPUT_DIR,
)
from cv.models.prediction import Prediction
from cv.services.detector import DetectorService
from cv.services.json_generator import JSONGenerator
from cv.services.severity import SeverityEngine
from cv.services.visualizer import Visualizer
from cv.utils.image_loader import ImageLoader


class PredictionPipeline:

    def __init__(self):
        self.detector = DetectorService(MODEL_PATH)
        self.severity = SeverityEngine()
        self.json_generator = JSONGenerator()
        self.visualizer = Visualizer()

    def run(self, image_path: Path):

        loader = ImageLoader(image_path)

        image = loader.load()

        height, width = image.shape[:2]

        detections = self.detector.detect(image)

        detections = self.severity.calculate(
            detections,
            width,
            height,
        )

        prediction = Prediction(
            image_name=image_path.name,
            image_width=width,
            image_height=height,
            model_name=MODEL_PATH.name,
            detections=detections,
        )

        json_path = self.json_generator.generate(
            prediction,
            JSON_OUTPUT_DIR,
        )

        annotated_path = IMAGE_OUTPUT_DIR / (
            image_path.stem + "_annotated.jpg"
        )

        self.visualizer.draw(
            image,
            detections,
            annotated_path,
        )

        return prediction, json_path, annotated_path


# ===========================
# Main Entry Point
# ===========================
if __name__ == "__main__":

    PROJECT_ROOT = Path(__file__).resolve().parents[2]

    image_path = PROJECT_ROOT / "data" / "raw" / "car3_test.jpg"

    pipeline = PredictionPipeline()

    prediction, json_path, image_output = pipeline.run(image_path)

    print("\nPrediction Completed Successfully!\n")

    print(f"JSON Report      : {json_path}")
    print(f"Annotated Image  : {image_output}")
    print(f"Total Detections : {len(prediction.detections)}")