from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Computer Vision
CV_DIR = PROJECT_ROOT / "cv"
MODEL_PATH = CV_DIR / "weights" / "best.pt"

# Data
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

CV_OUTPUT_DIR = PROJECT_ROOT / "cv" / "outputs"

JSON_OUTPUT_DIR = CV_OUTPUT_DIR / "json"

IMAGE_OUTPUT_DIR = CV_OUTPUT_DIR / "images"

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str

    PINECONE_API_KEY: str = ""
    PINECONE_INDEX_NAME: str = ""

    GROQ_API_KEY: str = ""
    GROQ_MODEL: str = "llama-3.1-8b-instant"

    SECRET_KEY: str = "change-this"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()