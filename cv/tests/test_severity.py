from dataclasses import asdict
from pathlib import Path

from configs.settings import MODEL_PATH
from cv.services.detector import DetectorService
from cv.services.severity import SeverityEngine
from cv.utils.image_loader import ImageLoader


PROJECT_ROOT = Path(__file__).resolve().parents[2]

IMAGE_PATH = PROJECT_ROOT / "data" / "raw" / "car_test.jpg"

loader = ImageLoader(IMAGE_PATH)

image = loader.load()

height, width = image.shape[:2]

detector = DetectorService(MODEL_PATH)

detections = detector.detect(image)

severity_engine = SeverityEngine()

results = severity_engine.calculate(
    detections,
    width,
    height
)

print()

for detection in results:
    print(asdict(detection))