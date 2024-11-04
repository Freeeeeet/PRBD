from fastapi import APIRouter, Depends, HTTPException, status, Header, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas
from app.crud.orders_crud import create_order, get_order, change_status, get_delivery_statuses, get_all_orders
from app.crud.users_crud import check_auth
from app.config import logger
router = APIRouter()


@router.get("/", response_model=list[schemas.OrderInfoResponse])
def read_all_orders(
    token: str = Header(...),
    db: Session = Depends(get_db),
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    authed_user = check_auth(db=db, token=token)
    if not authed_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    orders = get_all_orders(db=db, offset=offset, limit=limit)
    return orders


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


@router.get("/order_statuses", response_model=schemas.OrderDeliveryStatusesResponse)
def read_order_statuses_endpoint(token: str = Header(...), db: Session = Depends(get_db)):
    authed_user = check_auth(db=db, token=token)
    if not authed_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    statuses_response = get_delivery_statuses(db=db)
    if not statuses_response:
        raise HTTPException(status_code=404, detail="Order statuses not found")
    return statuses_response


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
