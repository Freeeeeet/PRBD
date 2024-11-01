from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import OrderCreateRequest, OrderCreateResponse
from app.crud.orders_crud import create_order
from app.crud.users_crud import check_auth
from app.config import logger
router = APIRouter()


@router.post("/create/", response_model=OrderCreateResponse)
def create_order_endpoint(order: OrderCreateRequest, db: Session = Depends(get_db)):
    authed_user = check_auth(db=db, token=order.token)

    if not authed_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    new_order = create_order(db=db, order=order, user_id=authed_user.id)
    logger.info(f"Order {new_order.id} created successfully!")
    return {"order_id": new_order.id}


# @router.get("/orders/{order_id}", response_model=OrderResponse)
# def read_order(order_id: int, db: Session = Depends(get_db)):
#     order = get_order(db=db, order_id=order_id)
#     if order is None:
#         raise HTTPException(status_code=404, detail="Order not found")
#     return order
#
#
# @router.put("/orders/{order_id}", response_model=OrderResponse)
# def update_order_endpoint(order_id: int, order_data: OrderCreate, db: Session = Depends(get_db)):
#     return update_order(db=db, order_id=order_id, order_data=order_data)
