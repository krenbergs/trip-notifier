from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class PostAccountRequest(BaseModel):
    gmail: str = Field(json_schema_extra={"example": "example@gmail.com"})
    created_at: int = Field(json_schema_extra={"example": "1704063600"})


class PostAccountSuccess(BaseModel):
    account_id: datetime = Field(json_schema_extra={"example": "15"})

    model_config = ConfigDict(from_attributes=True)


class PostAccountExists(BaseModel):
    detail: str = Field(json_schema_extra={"example": "Account already registered"})
