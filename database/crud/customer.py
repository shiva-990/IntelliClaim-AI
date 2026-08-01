from sqlalchemy.orm import Session

from database.models.customer import Customer
from database.schemas.customer import (
    CustomerCreate,
    CustomerUpdate,
)


def create_customer(
    db: Session,
    customer: CustomerCreate,
):
    db_customer = Customer(**customer.model_dump())

    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)

    return db_customer


def get_customer(
    db: Session,
    customer_id: str,
):
    return (
        db.query(Customer)
        .filter(Customer.customer_id == customer_id)
        .first()
    )


def get_all_customers(
    db: Session,
):
    return db.query(Customer).all()


def update_customer(
    db: Session,
    customer_id: str,
    customer: CustomerUpdate,
):
    db_customer = get_customer(
        db,
        customer_id,
    )

    if db_customer is None:
        return None

    update_data = customer.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(
            db_customer,
            key,
            value,
        )

    db.commit()
    db.refresh(db_customer)

    return db_customer


def delete_customer(
    db: Session,
    customer_id: str,
):
    db_customer = get_customer(
        db,
        customer_id,
    )

    if db_customer is None:
        return None

    db.delete(db_customer)
    db.commit()

    return db_customer