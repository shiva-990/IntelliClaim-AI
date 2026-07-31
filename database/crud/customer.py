from sqlalchemy.orm import Session

from database.models.customer import Customer
from database.schemas.customer import CustomerCreate


def create_customer(db: Session, customer: CustomerCreate):
    db_customer = Customer(
        customer_name=customer.customer_name,
        email=customer.email,
        phone=customer.phone,
        address=customer.address
    )

    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)

    return db_customer


def get_customer(db: Session, customer_id: int):
    return (
        db.query(Customer)
        .filter(Customer.customer_id == customer_id)
        .first()
    )


def get_all_customers(db: Session):
    return db.query(Customer).all()


def update_customer(
    db: Session,
    customer_id: int,
    customer: CustomerCreate
):
    db_customer = (
        db.query(Customer)
        .filter(Customer.customer_id == customer_id)
        .first()
    )

    if db_customer is None:
        return None

    db_customer.customer_name = customer.customer_name
    db_customer.email = customer.email
    db_customer.phone = customer.phone
    db_customer.address = customer.address

    db.commit()
    db.refresh(db_customer)

    return db_customer


def delete_customer(db: Session, customer_id: int):
    db_customer = (
        db.query(Customer)
        .filter(Customer.customer_id == customer_id)
        .first()
    )

    if db_customer is None:
        return None

    db.delete(db_customer)
    db.commit()

    return db_customer