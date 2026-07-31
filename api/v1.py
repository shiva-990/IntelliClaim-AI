from fastapi import APIRouter

from api.routes import (
    customer_router,
    vehicle_router,
    policy_router,
    claim_router,
    ai_decision_router,
    health_router,
    upload_router,
    detect_router,
    ai_detection_router,
)

api_v1_router = APIRouter(prefix="/api/v1")

api_v1_router.include_router(customer_router)
api_v1_router.include_router(vehicle_router)
api_v1_router.include_router(policy_router)
api_v1_router.include_router(claim_router)
api_v1_router.include_router(ai_decision_router)
api_v1_router.include_router(health_router)
api_v1_router.include_router(upload_router)
api_v1_router.include_router(detect_router)
api_v1_router.include_router(ai_detection_router)