"""
Deprecated.

Tables are now managed by Alembic migrations.
Do not use Base.metadata.create_all().
"""

from database.base import Base
from database.connection import engine

# Import all models
from database.models import *


def create_tables():

    Base.metadata.create_all(bind=engine)

    print("=" * 60)
    print("ALL TABLES CREATED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    create_tables() 