from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form,
    HTTPException,
    Depends,
)
from sqlalchemy.orm import Session

from database.connection import get_db
from database.crud.claim import (
    get_claim,
    update_cv_status,
)

from services.upload_service import save_claim_image


router = APIRouter(
    prefix="/upload",
    tags=["Image Upload"],
)


@router.post("/image")
def upload_image(

    claim_id: str = Form(...),

    image: UploadFile = File(...),

    db: Session = Depends(get_db),

):

    claim = get_claim(
        db,
        claim_id,
    )

    if claim is None:
        raise HTTPException(
            status_code=404,
            detail="Claim not found",
        )

    file_path = save_claim_image(
        claim_id,
        image,
    )

    update_cv_status(
        db,
        claim_id,
        "Uploaded",
    )

    return {

        "claim_id": claim_id,

        "filename": image.filename,

        "saved_path": file_path,

        "cv_status": "Uploaded",

    }