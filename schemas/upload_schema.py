from pydantic import BaseModel


class UploadResponse(BaseModel):
    message: str
    filename: str
    image_path: str
    status: str