import psycopg2
from src.settings import settings


def get_connection():
    return psycopg2.connect(
        dbname=settings.postgres_db,
        user=settings.postgres_user,
        password=settings.postgres_password,
        host=settings.postgres_host,
        port=settings.postgres_port,
    )


def show_all_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
    SELECT tablename
    FROM pg_catalog.pg_tables
    WHERE schemaname='public';
    """
    )

    tables = cursor.fetchall()

    for table in tables:
        print(f"---------[ {table[0]} ]---------")
        cursor.execute(f"SELECT * FROM {table[0]} LIMIT 10;")
        rows = cursor.fetchall()

        cursor.execute(
            f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table[0]}';"
        )
        columns = [desc[0] for desc in cursor.fetchall()]
        print(f"({', '.join(columns)})")

        for row in rows:
            print(row)
        print("\n")

    cursor.close()
    connection.close()


if __name__ == "__main__":
    show_all_tables()
