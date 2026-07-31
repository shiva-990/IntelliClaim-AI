from pathlib import Path

from fastapi import HTTPException, UploadFile

from schemas.upload_schema import UploadResponse
from utils.file_utils import (
    validate_image_extension,
    generate_unique_filename,
    ensure_upload_directory,
)


UPLOAD_DIRECTORY = "uploads/claims"


class UploadService:
    @staticmethod
    async def upload_image(file: UploadFile) -> UploadResponse:
        """
        Upload and save a vehicle damage image.
        """

        # Validate image type
        if not validate_image_extension(file.filename):
            raise HTTPException(
                status_code=400,
                detail="Only JPG, JPEG and PNG images are allowed."
            )

        # Ensure upload directory exists
        upload_dir = ensure_upload_directory(UPLOAD_DIRECTORY)

        # Generate unique filename
        filename = generate_unique_filename(file.filename)

        file_path = upload_dir / filename

        # Save file
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        return UploadResponse(
            message="Image uploaded successfully",
            filename=filename,
            image_path=str(file_path),
            status="uploaded"
        )