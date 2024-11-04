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
        if order:
            # Получение истории статусов заказа
            order_statuses = (
                db.query(models.DeliveryStatus.status_name, models.ShipmentHistory.created_at)
                .join(models.ShipmentHistory, models.Order.id == models.ShipmentHistory.order_id)
                .join(models.DeliveryStatus, models.DeliveryStatus.id == models.ShipmentHistory.status_id)
                .filter(models.Order.id == order_id)
                .all()
            )
            # Преобразование статусов в формат, подходящий для ответа
            order.order_statuses = [schemas.OrderStatus(status_name=status.status_name, created_at=status.created_at) for status
                                    in order_statuses]
        return order
    except Exception as e:
        logger.error(f"An error occurred while getting order {order_id} from db {e}", exc_info=True)
        return None


def change_status(db: Session, order_status: schemas.OrderChangeStatusRequest):
    try:
        new_status = models.ShipmentHistory(
            order_id=order_status.order_id,
            status_id=order_status.status_id
        )
        db.add(new_status)
        db.commit()
        db.refresh(new_status)
        logger.info(f"Delivery status for order {new_status.order_id} added to database correctly, returning new_status")
        return new_status
    except Exception as e:
        db.rollback()
        logger.error(f"An error occurred while adding new order status to DB. {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while adding new order status to the database."
        )



