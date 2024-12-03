from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class PostAccountRequest(BaseModel):
    phone_number: str = Field(json_schema_extra={"example": "467012345678"})
    subscribed: str = Field(json_schema_extra={"example": "0"})


class PostAccountSuccess(BaseModel):
    created_at: datetime = Field(json_schema_extra={"example": "2024-01-01T00:00:00"})

    model_config = ConfigDict(from_attributes=True)


class PostAccountExists(BaseModel):
    detail: str = Field(json_schema_extra={"example": "Account already registered"})
