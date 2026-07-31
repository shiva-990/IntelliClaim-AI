from pathlib import Path
from uuid import uuid4

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}


def validate_image_extension(filename: str) -> bool:
    extension = Path(filename).suffix.lower()
    return extension in ALLOWED_EXTENSIONS


def generate_unique_filename(filename: str) -> str:
    extension = Path(filename).suffix.lower()
    return f"{uuid4().hex}{extension}"


def ensure_upload_directory(upload_dir: str) -> Path:
    path = Path(upload_dir)
    path.mkdir(parents=True, exist_ok=True)
    return path