from sqlalchemy.orm import Session

from database.models.vehicle import Vehicle
from database.schemas.vehicle import (
    VehicleCreate,
)


def create_vehicle(
    db: Session,
    vehicle: VehicleCreate,
):

    db_vehicle = Vehicle(

        customer_id=vehicle.customer_id,

        registration_number=vehicle.registration_number,

        make=vehicle.make,

        model=vehicle.model,

        manufacture_year=vehicle.manufacture_year,
    )

    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)

    return db_vehicle


def get_vehicle(
    db: Session,
    vehicle_id: int,
):

    return (
        db.query(Vehicle)
        .filter(
            Vehicle.vehicle_id == vehicle_id
        )
        .first()
    )


def get_all_vehicles(db: Session):

    return db.query(Vehicle).all()


def update_vehicle(
    db: Session,
    vehicle_id: int,
    vehicle: VehicleCreate,
):

    db_vehicle = get_vehicle(
        db,
        vehicle_id,
    )

    if db_vehicle is None:
        return None

    db_vehicle.customer_id = vehicle.customer_id

    db_vehicle.registration_number = (
        vehicle.registration_number
    )

    db_vehicle.make = vehicle.make

    db_vehicle.model = vehicle.model

    db_vehicle.manufacture_year = (
        vehicle.manufacture_year
    )

    db.commit()
    db.refresh(db_vehicle)

    return db_vehicle


def delete_vehicle(
    db: Session,
    vehicle_id: int,
):

    db_vehicle = get_vehicle(
        db,
        vehicle_id,
    )

    if db_vehicle is None:
        return None

    db.delete(db_vehicle)
    db.commit()

    return db_vehicle