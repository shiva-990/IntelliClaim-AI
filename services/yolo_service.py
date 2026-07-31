from pathlib import Path
from unittest import result

from ultralytics import YOLO

from configs.settings import MODEL_PATH


class YOLOService:
    """
    Singleton YOLO Model Loader
    """

    _model = None

    @classmethod
    def load_model(cls):
        """
        Load model only once.
        """
        if cls._model is None:

            if not Path(MODEL_PATH).exists():
                raise FileNotFoundError(
                    f"YOLO model not found: {MODEL_PATH}"
                )

            cls._model = YOLO(str(MODEL_PATH))

            print("✅ YOLO model loaded successfully")

        return cls._model
    @classmethod
    def predict(cls, image_path: str):
        """
        Run YOLO inference on an image.
        """

        model = cls.load_model()

        results = model.predict(
            source=image_path,
            save=False,
            conf=0.30,
            verbose=False
        )

        return results
    @classmethod
    def parse_results(cls, results):

        parsed = []

        result = results[0]

        for box in result.boxes:

           cls_id = int(box.cls[0])

           parsed.append(
               {
                   "part": result.names[cls_id],
                   "confidence": round(
                       float(box.conf[0]),
                       2
                    ),
                    "bbox": [
                       float(x)
                       for x in box.xyxy[0]
                    ]
                }
            )
        return parsed