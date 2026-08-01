from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import get_db

from database.schemas.customer import (
    CustomerCreate,
    CustomerUpdate,
    CustomerResponse,
)

from database.crud.customer import (
    create_customer,
    get_customer,
    get_all_customers,
    update_customer,
    delete_customer,
)

router = APIRouter(
    prefix="/customers",
    tags=["Customers"],
)


@router.post("/", response_model=CustomerResponse)
def create_customer_api(
    customer: CustomerCreate,
    db: Session = Depends(get_db),
):

    existing = get_customer(db, customer.customer_id)

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Customer already exists",
        )

    return create_customer(db, customer)


@router.get("/", response_model=list[CustomerResponse])
def get_all_customers_api(
    db: Session = Depends(get_db),
):
    return get_all_customers(db)


@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer_api(
    customer_id: str,
    db: Session = Depends(get_db),
):

    customer = get_customer(db, customer_id)

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found",
        )

    return customer


@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer_api(
    customer_id: str,
    customer: CustomerUpdate,
    db: Session = Depends(get_db),
):

    updated = update_customer(
        db,
        customer_id,
        customer,
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found",
        )

    return updated


@router.delete("/{customer_id}")
def delete_customer_api(
    customer_id: str,
    db: Session = Depends(get_db),
):

    deleted = delete_customer(
        db,
        customer_id,
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found",
        )

    return {
        "message": "Customer deleted successfully"
    }