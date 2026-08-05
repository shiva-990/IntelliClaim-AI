from pathlib import Path

from sqlalchemy.orm import Session

from cv.scripts.predict import PredictionPipeline

from database.crud.ai_detection import (
    create_ai_detection,
    get_ai_detection_by_claim,
)

from database.crud.claim import update_cv_status

from database.schemas.ai_detection import (
    AIDetectionCreate,
)


class DetectionService:

    def __init__(self):
        self.pipeline = PredictionPipeline()

        # ----------------------------------------
        # Damage Cost Estimation (₹)
        # ----------------------------------------
        self.damage_cost = {
            "scratch": 5000,
            "dent": 12000,
            "light": 8000,
            "door": 25000,
            "fender": 20000,
            "bonnet": 30000,
            "bumper": 22000,
            "windshield": 18000,
            "smash": 60000,
        }

        # ----------------------------------------
        # Repair Days
        # ----------------------------------------
        self.damage_days = {
            "scratch": 2,
            "dent": 4,
            "light": 1,
            "door": 6,
            "fender": 5,
            "bonnet": 7,
            "bumper": 5,
            "windshield": 3,
            "smash": 12,
        }

    # -------------------------------------------------
    # Run YOLO Detection
    # -------------------------------------------------
    def detect_claim(
        self,
        claim_id: str,
    ):

        claim_folder = Path("uploads") / "claims" / claim_id

        if not claim_folder.exists():
            raise FileNotFoundError(
                f"Claim folder not found: {claim_folder}"
            )

        image_paths = []

        for extension in ("*.jpg", "*.jpeg", "*.png"):
            image_paths.extend(
                claim_folder.glob(extension)
            )

        if not image_paths:
            raise FileNotFoundError(
                "No images found for this claim."
            )

        predictions = []

        for image_path in sorted(image_paths):

            prediction = self.pipeline.run(
                image_path
            )

            predictions.append(
                prediction
            )

        return predictions

    # -------------------------------------------------
    # Save Detection Results
    # -------------------------------------------------
    def save_results(
        self,
        db: Session,
        claim_id: str,
        predictions,
    ):

        existing = get_ai_detection_by_claim(
            db,
            claim_id,
        )

        if existing:
            print(
                f"[CV] Detection already exists for {claim_id}"
            )
            return existing

        print(
            f"[CV] Saving detections for claim {claim_id}"
        )

        saved = []

        for prediction in predictions:

            detections = [
                detection.to_dict()
                for detection in prediction.detections
            ]

            # ----------------------------------------
            # Default Values
            # ----------------------------------------

            severity = "Low"

            repair_cost = 0

            repair_days = 0

            repairable = True

            # ----------------------------------------
            # Calculate Repair Cost & Days
            # ----------------------------------------

            for detection in detections:

                damage = detection["class_name"].lower()

                repair_cost += self.damage_cost.get(
                    damage,
                    0,
                )

                repair_days = max(
                    repair_days,
                    self.damage_days.get(
                        damage,
                        0,
                    ),
                )

            # ----------------------------------------
            # Severity
            # ----------------------------------------

            if any(
                d["class_name"].lower() == "smash"
                for d in detections
            ):
                severity = "High"

            elif any(
                d["class_name"].lower() == "dent"
                for d in detections
            ):
                severity = "Medium"

            else:
                severity = "Low"

            # ----------------------------------------
            # Repairable Logic
            # ----------------------------------------

            if repair_cost > 100000:
                repairable = False

            # ----------------------------------------
            # Save Detection
            # ----------------------------------------

            db_detection = AIDetectionCreate(

                claim_id=claim_id,

                image_name=prediction.image_name,

                detections=detections,

                severity=severity,

                repair_cost=repair_cost,

                repair_days=repair_days,

                repairable=repairable,
            )

            saved_detection = create_ai_detection(
                db,
                db_detection,
            )

            saved.append(
                saved_detection
            )

            print(
                f"[CV] Saved {prediction.image_name}"
            )

            print(
                f"     Severity     : {severity}"
            )

            print(
                f"     Repair Cost  : ₹{repair_cost}"
            )

            print(
                f"     Repair Days  : {repair_days}"
            )

        update_cv_status(
            db,
            claim_id,
            "Completed",
        )

        print(
            f"[CV] Total detections saved: {len(saved)}"
        )

        return saved