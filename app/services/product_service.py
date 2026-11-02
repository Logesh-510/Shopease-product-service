
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.models.product_db_model import ProductDB


# Create Product
def create_product(db: Session, product_data: dict):
    try:
        new_product = ProductDB(**product_data)

        db.add(new_product)
        db.commit()
        db.refresh(new_product)

        return new_product

    except SQLAlchemyError:
        db.rollback()
        raise


# Get All Products
def get_all_products(db: Session, status: str | None = None):
    query = db.query(ProductDB)

    if status is not None:
        query = query.filter(ProductDB.status == status)

    return query.all()


# Get Product By ID
def get_product_by_id(db: Session, product_id: int):
    return (
        db.query(ProductDB)
        .filter(ProductDB.id == product_id)
        .first()
    )


# Update Product
def update_product(
    db: Session,
    product_id: int,
    update_data: dict
):
    product = get_product_by_id(db, product_id)

    if product is None:
        return None

    try:
        for key, value in update_data.items():
            setattr(product, key, value)

        db.commit()
        db.refresh(product)

        return product

    except SQLAlchemyError:
        db.rollback()
        raise


# Delete Product (Soft Delete)
def delete_product(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)

    if product is None:
        return None

    try:
        product.status = "Inactive"

        db.commit()
        db.refresh(product)

        return product

    except SQLAlchemyError:
        db.rollback()
        raise
