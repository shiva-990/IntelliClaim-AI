from pathlib import Path

from configs.settings import (
    IMAGE_OUTPUT_DIR,
    MODEL_PATH,
)
from cv.services.detector import DetectorService
from cv.services.severity import SeverityEngine
from cv.services.visualizer import Visualizer
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

visualizer = Visualizer()

output_path = IMAGE_OUTPUT_DIR / "car_test_annotated.jpg"

visualizer.draw(
    image,
    detections,
    output_path,
)

print(f"\nAnnotated image saved to:\n{output_path}")