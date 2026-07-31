from pathlib import Path

from configs.settings import MODEL_PATH
from cv.services.detector import DetectorService
from cv.utils.image_loader import ImageLoader


PROJECT_ROOT = Path(__file__).resolve().parents[2]

IMAGE_PATH = PROJECT_ROOT / "data" / "raw" / "car3_test.jpg"


loader = ImageLoader(IMAGE_PATH)

image = loader.load()

detector = DetectorService(MODEL_PATH)

detections = detector.detect(image)

print("\nDetections:\n")

for detection in detections:
    print(detection.to_dict())