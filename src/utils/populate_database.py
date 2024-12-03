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
    account1 = AccountTable(phone_number="467012345689", subscribed=False)
    account2 = AccountTable(phone_number="467312456789", subscribed=True)

    session.add_all([account1, account2])
    session.commit()


if __name__ == "__main__":
    populate_db()
