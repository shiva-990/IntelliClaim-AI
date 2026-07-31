from pathlib import Path

from cv.utils.image_loader import ImageLoader


PROJECT_ROOT = Path(__file__).resolve().parents[2]

IMAGE_PATH = PROJECT_ROOT / "data" / "raw" / "car3_test.jpg"


loader = ImageLoader(IMAGE_PATH)

image = loader.load()

print("Image Loaded Successfully!")

print(loader.metadata())