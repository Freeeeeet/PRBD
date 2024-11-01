from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.config import logger
from app import models, schemas
from app.utils.genaral_utils import create_tracking_number


def create_order(db: Session, order: schemas.OrderCreateRequest, user_id: int):
    try:
        tracking_number = create_tracking_number()
        db_order = models.Order(
            weight=order.weight,
            source_location=order.source_location,
            destination_location=order.destination_location,
            tracking_number=tracking_number,
            total_price=order.total_price,
            user_id=user_id
        )
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        logger.info(f"Order {db_order.id} added to database correctly, returning order_id")
        return db_order
    except Exception as e:
        db.rollback()
        logger.error(f"An error occurred while adding order to DB. {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while adding order to the database."
        )


def get_order(db: Session, order_id: int):
    try:
        order = db.query(models.Order).filter(models.Order.id == order_id).first()
        return order
    except Exception as e:
        logger.error(f"An error occurred while getting order {order_id} from db {e}", exc_info=True)
        return None

