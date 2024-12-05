from sqlalchemy import Column, DateTime, Integer, String, Boolean
from datetime import datetime, timezone
from src.database.database import Base


class AccountTable(Base):
    __tablename__ = "account"
    account_id = Column(Integer, primary_key=True, autoincrement=True)
    gmail = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    subscribed = Column(Boolean, default=False)