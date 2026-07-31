from fastapi import APIRouter
from sqlalchemy import text

from api.deps import DBSession

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
def health_check(db: DBSession):
    try:
        db.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "service": "IntelliClaim AI",
            "database": "connected"
        }

    except Exception:
        return {
            "status": "unhealthy",
            "service": "IntelliClaim AI",
            "database": "disconnected"
        }