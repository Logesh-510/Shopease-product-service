
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.product_schema import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)
from app.services import product_service


router = APIRouter(
    prefix="/api/v1/products",
    tags=["Products"]
)


# Product Router Health Check
@router.get("/health")
def product_router_health():
    return {
        "message": "Product Router is working",
        "status": "success"
    }


# Create Product
@router.post(
    "/",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
def create_product(
    product_data: ProductCreate,
    db: Session = Depends(get_db)
):
    return product_service.create_product(
        db,
        product_data.model_dump()
    )


# Get All Products
@router.get("/", response_model=list[ProductResponse])
def get_all_products(
    status: str | None = None,
    db: Session = Depends(get_db)
):
    if status is not None and status not in ["Active", "Inactive"]:
        raise HTTPException(
            status_code=400,
            detail="Status must be Active or Inactive"
        )

    return product_service.get_all_products(
        db,
        status
    )


# Get Product By ID
@router.get("/{product_id}", response_model=ProductResponse)
def get_product_by_id(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = product_service.get_product_by_id(
        db,
        product_id
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


# Update Product
@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    product_data: ProductUpdate,
    db: Session = Depends(get_db)
):
    update_data = product_data.model_dump(
        exclude_unset=True,
        exclude_none=True
    )

    product = product_service.update_product(
        db,
        product_id,
        update_data
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


# Delete Product (Soft Delete)
@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = product_service.delete_product(
        db,
        product_id
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "message": "Product deactivated successfully",
        "product_id": product_id,
        "status": product.status
    }
