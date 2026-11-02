from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Literal


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1)
    description: str | None = None
    price: float = Field(..., gt=0)
    stock_quantity: int = Field(..., ge=0)
    category: str = Field(..., min_length=1)

    @field_validator("name", "category")
    @classmethod
    def validate_text(cls, value):
        if not value.strip():
            raise ValueError("This field cannot contain only spaces")
        return value.strip()

class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1)
    description: str | None = None
    price: float | None = Field(default=None, gt=0)
    stock_quantity: int | None = Field(default=None, ge=0)
    category: str | None = Field(default=None, min_length=1)
    status: Literal["Active", "Inactive"] | None = None

    @field_validator("name", "category")
    @classmethod
    def validate_text(cls, value):
        if value is None:
            return value

        if not value.strip():
            raise ValueError("This field cannot contain only spaces")

        return value.strip()

class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str | None
    price: float
    stock_quantity: int
    category: str
    status: Literal["Active", "Inactive"]
    created_at: datetime
