from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field, field_validator


class Product(BaseModel):
    id: int
    name: str = Field(..., min_length=1)
    description: str | None = None
    price: float = Field(..., gt=0)
    stock_quantity: int = Field(..., ge=0)
    category: str = Field(..., min_length=1)
    status: Literal["Active", "Inactive"] = "Active"
    created_at: datetime = Field(default_factory=datetime.now)

    @field_validator("name", "category")
    @classmethod
    def validate_text(cls, value):
        if not value.strip():
            raise ValueError("This field cannot contain only spaces")
        return value.strip()
