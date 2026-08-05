from fastapi import APIRouter, Depends

from database.session import get_db

from services.report_service import ReportService

router = APIRouter()

service = ReportService()


@router.get(
    "/report/{claim_id}",
)
def report(
    claim_id: str,
    db=Depends(get_db),
):

    return service.build_report(
        db,
        claim_id,
    )