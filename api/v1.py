from fastapi import APIRouter

from api.routes import (
    customer_router,
    policy_router,
    claim_router,
    upload_router,
    detect_router,
    nlp_router,
    ai_detection_router,
    ai_decision_router,
    health_router,
    vehicle_router,
    process_claim_router,
    report_router,
    claim_history_router,
)

api_v1_router = APIRouter(prefix="/api/v1")

# Master Data
api_v1_router.include_router(customer_router)
api_v1_router.include_router(policy_router)
api_v1_router.include_router(claim_router)
api_v1_router.include_router(vehicle_router)
# AI Processing
api_v1_router.include_router(upload_router)
api_v1_router.include_router(detect_router)
api_v1_router.include_router(nlp_router)

# AI Results
api_v1_router.include_router(ai_detection_router)
api_v1_router.include_router(ai_decision_router)

# Health
api_v1_router.include_router(health_router)

api_v1_router.include_router(
    process_claim_router
)
api_v1_router.include_router(report_router)
api_v1_router.include_router(
    report_router,
    prefix="/reports",
    tags=["Reports"],
)
api_v1_router.include_router(
    claim_history_router
)