from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime, timezone
from src.database.database import Base


class AccountTable(Base):
    __tablename__ = "account"
    phone_number = Column(String(12), primary_key=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    subscribed = Column(Boolean, default=False)
