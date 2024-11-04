from fastapi import APIRouter, Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas
from app.crud.orders_crud import create_order, get_order, change_status, get_delivery_statuses
from app.crud.users_crud import check_auth
from app.config import logger
router = APIRouter()


@router.post("/create/", response_model=schemas.OrderCreateResponse)
def create_order_endpoint(order: schemas.OrderCreateRequest, token: str = Header(...), db: Session = Depends(get_db)):
    authed_user = check_auth(db=db, token=token)
    if not authed_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    new_order = create_order(db=db, order=order, user_id=authed_user.id)
    logger.info(f"Order {new_order.id} created successfully!")
    return {"order_id": new_order.id}


@router.get("/{order_id}", response_model=schemas.OrderInfoResponse)
def read_order_endpoint(order_id: int, token: str = Header(...), db: Session = Depends(get_db)):
    authed_user = check_auth(db=db, token=token)
    if not authed_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    order = get_order(db=db, order_id=order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.post("/change_order_status/", response_model=schemas.OrderChangeStatusResponse)
def change_order_status_endpoint(order_status: schemas.OrderChangeStatusRequest, token: str = Header(...),
                                 db: Session = Depends(get_db)):
    authed_user = check_auth(db=db, token=token)
    if not authed_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    change_status(db=db, order_status=order_status)
    return {"success": True}


@router.get("/order_statuses", response_model=schemas.OrderDeliveryStatusesResponse)
def read_order_statuses_endpoint(token: str = Header(...), db: Session = Depends(get_db)):
    authed_user = check_auth(db=db, token=token)
    if not authed_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    statuses = get_delivery_statuses(db=db)
    if not statuses:
        raise HTTPException(status_code=404, detail="Order statuses not found")
    return {"statuses": statuses}


# @router.put("/orders/{order_id}", response_model=OrderResponse)
# def update_order_endpoint(order_id: int, order_data: OrderCreate, db: Session = Depends(get_db)):
#     return update_order(db=db, order_id=order_id, order_data=order_data)
