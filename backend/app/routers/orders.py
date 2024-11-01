from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import OrderCreate, OrderResponse
from app.crud.crud import create_order, get_order, delete_order_by_id, update_order

router = APIRouter()

@router.post("/orders/", response_model=OrderResponse)
def create_order_endpoint(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db=db, order=order)

@router.get("/orders/{order_id}", response_model=OrderResponse)
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = get_order(db=db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.delete("/orders/{order_id}", response_model=dict)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    return delete_order_by_id(db=db, order_id=order_id)

@router.put("/orders/{order_id}", response_model=OrderResponse)
def update_order_endpoint(order_id: int, order_data: OrderCreate, db: Session = Depends(get_db)):
    return update_order(db=db, order_id=order_id, order_data=order_data)