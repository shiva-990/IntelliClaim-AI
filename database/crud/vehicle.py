from sqlalchemy.orm import Session

from database.models.vehicle import Vehicle
from database.schemas.vehicle import VehicleCreate


def create_vehicle(db: Session, vehicle: VehicleCreate):
    db_vehicle = Vehicle(
        customer_id=vehicle.customer_id,
        policy_id=vehicle.policy_id,
        vehicle_number=vehicle.vehicle_number,
        make=vehicle.make,
        model=vehicle.model,
        year=vehicle.year,
        fuel_type=vehicle.fuel_type,
        vehicle_type=vehicle.vehicle_type
    )

    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)

    return db_vehicle


def get_vehicle(db: Session, vehicle_id: int):
    return (
        db.query(Vehicle)
        .filter(Vehicle.vehicle_id == vehicle_id)
        .first()
    )


def get_all_vehicles(db: Session):
    return db.query(Vehicle).all()


def update_vehicle(
    db: Session,
    vehicle_id: int,
    vehicle: VehicleCreate
):
    db_vehicle = (
        db.query(Vehicle)
        .filter(Vehicle.vehicle_id == vehicle_id)
        .first()
    )

    if db_vehicle is None:
        return None

    db_vehicle.customer_id = vehicle.customer_id
    db_vehicle.policy_id = vehicle.policy_id
    db_vehicle.vehicle_number = vehicle.vehicle_number
    db_vehicle.make = vehicle.make
    db_vehicle.model = vehicle.model
    db_vehicle.year = vehicle.year
    db_vehicle.fuel_type = vehicle.fuel_type
    db_vehicle.vehicle_type = vehicle.vehicle_type

    db.commit()
    db.refresh(db_vehicle)

    return db_vehicle


def delete_vehicle(db: Session, vehicle_id: int):
    db_vehicle = (
        db.query(Vehicle)
        .filter(Vehicle.vehicle_id == vehicle_id)
        .first()
    )

    if db_vehicle is None:
        return None

    db.delete(db_vehicle)
    db.commit()

    return db_vehicle