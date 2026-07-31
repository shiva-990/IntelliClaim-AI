from pathlib import Path

from configs.settings import (
    MODEL_PATH,
    JSON_OUTPUT_DIR,
)
from cv.models.prediction import Prediction
from cv.services.detector import DetectorService
from cv.services.json_generator import JSONGenerator
from cv.services.severity import SeverityEngine
from cv.utils.image_loader import ImageLoader


PROJECT_ROOT = Path(__file__).resolve().parents[2]

IMAGE_PATH = PROJECT_ROOT / "data" / "raw" / "car3_test.jpg"

loader = ImageLoader(IMAGE_PATH)

image = loader.load()

height, width = image.shape[:2]

detector = DetectorService(MODEL_PATH)

detections = detector.detect(image)

severity = SeverityEngine()

detections = severity.calculate(
    detections,
    width,
    height,
)

prediction = Prediction(
    image_name=IMAGE_PATH.name,
    image_width=width,
    image_height=height,
    model_name=MODEL_PATH.name,
    detections=detections,
)

generator = JSONGenerator()

output_path = generator.generate(
    prediction,
    JSON_OUTPUT_DIR,
)

print(f"\nJSON saved to:\n{output_path}")