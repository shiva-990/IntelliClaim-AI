from database.connection import SessionLocal


def get_db():
    """
    Dependency to provide a database session.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()