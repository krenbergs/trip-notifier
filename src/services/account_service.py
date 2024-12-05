from sqlalchemy.orm import Session
from src.database.account import AccountTable
from src.api.account.schemas import PostAccountRequest, PostAccountSuccess
from src.database.database import SessionLocal
from fastapi import HTTPException
from datetime import datetime

def create_account(account: PostAccountRequest) -> PostAccountSuccess:
    db: Session = SessionLocal()
    try:
        db_account = (
            db.query(AccountTable)
            .filter((AccountTable.gmail == account.gmail))
            .first()
        )

        if db_account:
            raise HTTPException(status_code=409, detail="Account already registered")

        new_account = AccountTable(
            gmail=account.gmail
        )
        if account.created_at:
            new_account.created_at = datetime.fromtimestamp(int(account.created_at))
        
        db.add(new_account)
        db.commit()
        db.refresh(new_account)
        return PostAccountSuccess.model_validate(new_account)

    except Exception as e:
        db.rollback()
        raise e

    finally:
        db.close()
