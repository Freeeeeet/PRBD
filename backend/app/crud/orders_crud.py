from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import List

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

        order_status = schemas.OrderChangeStatusRequest(order_id=db_order.id, status_id=1)
        change_status(db=db, order_status=order_status)
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
        order = db.query(
            models.Order).filter(models.Order.id == order_id).first()
        if order:
            # Получение истории статусов заказа
            order_statuses = (
                db.query(
                    models.Order.id,
                    models.DeliveryStatus.status_name,
                    models.ShipmentHistory.created_at
                )
                .join(models.ShipmentHistory, models.ShipmentHistory.order_id == models.Order.id)
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


def get_all_orders(db: Session, offset: int = 0, limit: int = 10) -> List[schemas.OrderInfoResponse]:
    try:
        # Основной запрос, загружающий заказы вместе со статусами
        orders = (
            db.query(
                models.Order.id,
                models.Order.weight,
                models.Order.source_location,
                models.Order.destination_location,
                models.Order.tracking_number,
                models.Order.total_price,
                models.Order.created_at,
                models.DeliveryStatus.status_name,
                models.DeliveryStatus.description,
                models.ShipmentHistory.created_at.label("status_created_at")
            )
            .outerjoin(models.ShipmentHistory, models.ShipmentHistory.order_id == models.Order.id)
            .outerjoin(models.DeliveryStatus, models.DeliveryStatus.id == models.ShipmentHistory.status_id)
            .offset(offset)
            .limit(limit)
            .all()
        )

        # Преобразование результатов в нужный формат
        result = []
        orders_dict = {}

        for order in orders:
            order_id = order.id
            if order_id not in orders_dict:
                # Создаем основной объект заказа с пустым списком статусов
                orders_dict[order_id] = schemas.OrderInfoResponse(
                    id=order.id,
                    weight=order.weight,
                    source_location=order.source_location,
                    destination_location=order.destination_location,
                    tracking_number=order.tracking_number,
                    total_price=order.total_price,
                    created_at=order.created_at,
                    order_statuses=[]
                )

            # Добавляем статус к соответствующему заказу
            if order.status_name:
                order_status = schemas.OrderStatus(
                    status_name=order.status_name,
                    description=order.description,
                    created_at=order.status_created_at
                )
                orders_dict[order_id].order_statuses.append(order_status)

        # Преобразование dict значений в список
        result = list(orders_dict.values())
        return result

    except Exception as e:
        logger.error(f"An error occurred while getting all orders from db {e}", exc_info=True)
        return []


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


def get_delivery_statuses(db: Session):
    try:
        statuses = db.query(models.DeliveryStatus).all()

        if statuses:
            statuses = [
                schemas.OrderDeliveryStatusResponse(
                    id=status_item.id,
                    status_name=status_item.status_name,
                    description=status_item.description
                ) for status_item in statuses
            ]
        return schemas.OrderDeliveryStatusesResponse(statuses=statuses)
    except Exception as e:
        logger.error(f"An error occurred while getting all order delivery statuses from db {e}", exc_info=True)
        return None

