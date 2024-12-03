from sqlalchemy.orm import Session
from src.database.account import AccountTable
from src.api.account.schemas import PostAccountRequest, PostAccountSuccess
from src.database.database import SessionLocal
from fastapi import HTTPException


def create_account(account: PostAccountRequest) -> PostAccountSuccess:
    db: Session = SessionLocal()
    try:
        db_account = (
            db.query(AccountTable)
            .filter((AccountTable.phone_number == account.phone_number))
            .first()
        )

        if db_account:
            raise HTTPException(status_code=409, detail="Account already registered")

        subscribed_bool = bool(int(account.subscribed))

        new_account = AccountTable(
            phone_number=account.phone_number, subscribed=subscribed_bool
        )
        db.add(new_account)
        db.commit()
        db.refresh(new_account)
        return PostAccountSuccess.model_validate(new_account)

    except Exception as e:
        db.rollback()
        raise e

    finally:
        db.close()
