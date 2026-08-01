from pathlib import Path
import shutil

from fastapi import UploadFile


# Root upload directory
UPLOAD_DIR = Path("uploads/claims")


def save_claim_image(
    claim_id: str,
    image: UploadFile,
) -> str:
    """
    Save uploaded image under:

    uploads/
        claims/
            CLM000001/
                image.jpg
    """

    # Create claim folder if it doesn't exist
    claim_folder = UPLOAD_DIR / claim_id

    claim_folder.mkdir(
        parents=True,
        exist_ok=True,
    )

    # Save image
    file_path = claim_folder / image.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            image.file,
            buffer,
        )

    return str(file_path)