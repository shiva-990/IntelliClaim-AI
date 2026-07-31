from fastapi import APIRouter, HTTPException

from api.deps import DBSession
from database.crud import vehicle as vehicle_crud
from database.schemas.vehicle import (
    VehicleCreate,
    VehicleResponse,
)

router = APIRouter(
    prefix="/vehicles",
    tags=["Vehicles"]
)


@router.post("/", response_model=VehicleResponse)
def create_vehicle_api(
    vehicle: VehicleCreate,
    db: DBSession
):
    return vehicle_crud.create_vehicle(db, vehicle)


@router.get("/", response_model=list[VehicleResponse])
def get_all_vehicles_api(
    db: DBSession
):
    return vehicle_crud.get_all_vehicles(db)


@router.get("/{vehicle_id}", response_model=VehicleResponse)
def get_vehicle_api(
    vehicle_id: int,
    db: DBSession
):
    vehicle = vehicle_crud.get_vehicle(db, vehicle_id)

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    return vehicle


@router.put("/{vehicle_id}", response_model=VehicleResponse)
def update_vehicle_api(
    vehicle_id: int,
    vehicle: VehicleCreate,
    db: DBSession
):
    updated_vehicle = vehicle_crud.update_vehicle(
        db,
        vehicle_id,
        vehicle
    )

    if updated_vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    return updated_vehicle


@router.delete("/{vehicle_id}")
def delete_vehicle_api(
    vehicle_id: int,
    db: DBSession
):
    deleted_vehicle = vehicle_crud.delete_vehicle(
        db,
        vehicle_id
    )

    if deleted_vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    return {
        "message": "Vehicle deleted successfully"
    }