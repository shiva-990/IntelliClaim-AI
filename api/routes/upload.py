from fastapi import APIRouter, File, UploadFile

from schemas.upload_schema import UploadResponse
from services.upload_service import UploadService

upload_router = APIRouter(
    prefix="/upload",
    tags=["Image Upload"]
)


@upload_router.post(
    "/image",
    response_model=UploadResponse,
    summary="Upload Vehicle Damage Image"
)
async def upload_image(file: UploadFile = File(...)):
    """
    Upload a vehicle damage image.
    """
    return await UploadService.upload_image(file)
print("✅ Upload router loaded")