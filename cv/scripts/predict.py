from pathlib import Path
import cv2

from configs.settings import MODEL_PATH
from cv.models.prediction import Prediction
from cv.services.detector import DetectorService


class PredictionPipeline:

    def __init__(self):
        self.detector = DetectorService(MODEL_PATH)

    def run(self, image_path: Path):

        image = cv2.imread(str(image_path))

        if image is None:
            raise FileNotFoundError(
                f"Unable to load image: {image_path}"
            )

        height, width = image.shape[:2]

        detections = self.detector.detect(image)

        prediction = Prediction(
            image_name=image_path.name,
            image_width=width,
            image_height=height,
            model_name=MODEL_PATH.name,
            detections=detections,
        )

        return prediction


if __name__ == "__main__":

    image_path = Path("data/raw/car3_test.jpg")

    pipeline = PredictionPipeline()

    prediction = pipeline.run(image_path)

    print("=" * 60)
    print("Prediction Successful")
    print("=" * 60)

    print(f"Image : {prediction.image_name}")
    print(f"Total Detections : {len(prediction.detections)}")

    for detection in prediction.detections:
        print(detection.to_dict())