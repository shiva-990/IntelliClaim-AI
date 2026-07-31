from pathlib import Path
import cv2


SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp"}


class ImageLoader:
    """
    Handles image validation and loading.
    """

    def __init__(self, image_path):
        self.image_path = Path(image_path)

    def validate(self):
        """
        Validate image path and format.
        """

        if not self.image_path.exists():
            raise FileNotFoundError(
                f"Image not found: {self.image_path}"
            )

        if self.image_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Unsupported image format: {self.image_path.suffix}"
            )

    def load(self):
        """
        Load image using OpenCV.
        """

        self.validate()

        image = cv2.imread(str(self.image_path))

        if image is None:
            raise ValueError(
                "OpenCV failed to read the image."
            )

        return image

    def metadata(self):
        """
        Return image metadata.
        """

        image = self.load()

        height, width = image.shape[:2]

        return {
            "filename": self.image_path.name,
            "path": str(self.image_path),
            "width": width,
            "height": height,
            "channels": image.shape[2] if len(image.shape) == 3 else 1
        }
    