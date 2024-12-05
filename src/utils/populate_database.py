from sqlalchemy.orm import sessionmaker
from src.database import (
    Base,
    AccountTable,
)
from src.database.database import engine

Session = sessionmaker(bind=engine)
session = Session()


def populate_db():
    # Add Accounts
    account1 = AccountTable(gmail="hamliannu@gmail.com")
    account2 = AccountTable(gmail="")

    session.add_all([account1, account2])
    session.commit()


if __name__ == "__main__":
    populate_db()
