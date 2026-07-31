from fastapi import APIRouter, HTTPException

from configs.logger import logger
from api.deps import DBSession

from database.crud.customer import (
    create_customer,
    get_customer,
    get_all_customers,
    update_customer,
    delete_customer,
)

from database.schemas.customer import (
    CustomerCreate,
    CustomerResponse,
)

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.post("/", response_model=CustomerResponse)
def create_customer_api(
    customer: CustomerCreate,
    db: DBSession
):
    logger.info("Creating a new customer")

    try:
        created_customer = create_customer(db, customer)

        logger.info(
            f"Customer created successfully. ID={created_customer.customer_id}"
        )

        return created_customer

    except Exception as e:
        logger.exception(f"Failed to create customer: {e}")
        raise


@router.get("/", response_model=list[CustomerResponse])
def get_all_customers_api(
    db: DBSession
):
    logger.info("Fetching all customers")

    try:
        customers = get_all_customers(db)

        logger.info(
            f"Retrieved {len(customers)} customers"
        )

        return customers

    except Exception as e:
        logger.exception(f"Failed to fetch customers: {e}")
        raise


@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer_api(
    customer_id: int,
    db: DBSession
):
    logger.info(f"Fetching customer with ID={customer_id}")

    try:
        customer = get_customer(db, customer_id)

        if customer is None:
            logger.warning(f"Customer {customer_id} not found")

            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )

        logger.info(
            f"Customer {customer_id} fetched successfully"
        )

        return customer

    except HTTPException:
        raise

    except Exception as e:
        logger.exception(
            f"Error while fetching customer {customer_id}: {e}"
        )
        raise


@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer_api(
    customer_id: int,
    customer: CustomerCreate,
    db: DBSession
):
    logger.info(f"Updating customer {customer_id}")

    try:
        updated_customer = update_customer(
            db,
            customer_id,
            customer
        )

        if updated_customer is None:
            logger.warning(
                f"Customer {customer_id} not found for update"
            )

            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )

        logger.info(
            f"Customer {customer_id} updated successfully"
        )

        return updated_customer

    except HTTPException:
        raise

    except Exception as e:
        logger.exception(
            f"Error while updating customer {customer_id}: {e}"
        )
        raise


@router.delete("/{customer_id}")
def delete_customer_api(
    customer_id: int,
    db: DBSession
):
    logger.info(f"Deleting customer {customer_id}")

    try:
        deleted_customer = delete_customer(
            db,
            customer_id
        )

        if deleted_customer is None:
            logger.warning(
                f"Customer {customer_id} not found for deletion"
            )

            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )

        logger.info(
            f"Customer {customer_id} deleted successfully"
        )

        return {
            "message": "Customer deleted successfully"
        }

    except HTTPException:
        raise

    except Exception as e:
        logger.exception(
            f"Error while deleting customer {customer_id}: {e}"
        )
        raise