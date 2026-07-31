from fastapi import APIRouter, HTTPException

from schemas.detection_schema import DetectionResponse
from services.yolo_service import YOLOService

router = APIRouter(
    prefix="/detect",
    tags=["Damage Detection"]
)


@router.post(
    "/damage",
    response_model=DetectionResponse
)
def detect_damage(image_path: str):

    try:

        results = YOLOService.predict(image_path)

        detections = YOLOService.parse_results(results)

        return DetectionResponse(
            filename=image_path.split("/")[-1].split("\\")[-1],
            detections=detections
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )