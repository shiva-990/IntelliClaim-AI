from pathlib import Path

from sqlalchemy.orm import Session

from cv.scripts.predict import PredictionPipeline

from database.schemas.ai_detection import AIDetectionCreate
from database.crud.ai_detection import create_ai_detection
from database.crud.claim import update_cv_status


class DetectionService:

    def __init__(self):
        self.pipeline = PredictionPipeline()

    # Existing method
    def detect_claim(self, claim_id: str):

        claim_folder = Path("uploads") / "claims" / claim_id

        if not claim_folder.exists():
            raise FileNotFoundError(
                f"Claim folder not found: {claim_folder}"
            )

        image_paths = []

        for extension in ("*.jpg", "*.jpeg", "*.png"):
            image_paths.extend(claim_folder.glob(extension))

        if not image_paths:
            raise FileNotFoundError(
                "No images found for this claim."
            )

        predictions = []

        for image_path in sorted(image_paths):
            prediction = self.pipeline.run(image_path)
            predictions.append(prediction)

        return predictions

    # 👇 ADD THIS NEW METHOD HERE
    def save_results(
        self,
        db: Session,
        claim_id: str,
        predictions,
    ):

        saved = []

        for prediction in predictions:

            detections = [
                d.to_dict()
                for d in prediction.detections
            ]

            severity = "Low"

            if any(
                d["class_name"] == "smash"
                for d in detections
            ):
                severity = "High"

            elif any(
                d["class_name"] == "dent"
                for d in detections
            ):
                severity = "Medium"

            detection = AIDetectionCreate(
                claim_id=claim_id,
                image_name=prediction.image_name,
                detections=detections,
                severity=severity,
                repair_cost=0,
                repair_days=0,
                repairable=True,
            )

            saved.append(
                create_ai_detection(
                    db,
                    detection,
                )
            )

        update_cv_status(
            db,
            claim_id,
            "Completed",
        )

        return saved