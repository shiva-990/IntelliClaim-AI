from sqlalchemy import text

from database.connection import engine


def test_connection():

    try:

        with engine.connect() as connection:

            result = connection.execute(text("SELECT version();"))

            print("=" * 60)
            print("POSTGRESQL CONNECTED SUCCESSFULLY")
            print("=" * 60)

            print(result.scalar())

    except Exception as e:

        print("=" * 60)
        print("DATABASE CONNECTION FAILED")
        print("=" * 60)

        print(e)


if __name__ == "__main__":
    test_connection()