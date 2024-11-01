from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import PaymentCreate, PaymentResponse
from app.crud.crud import create_payment, get_payment, delete_payment_by_id, update_payment

router = APIRouter()

@router.post("/payments/", response_model=PaymentResponse)
def create_payment_endpoint(payment: PaymentCreate, db: Session = Depends(get_db)):
    return create_payment(db=db, payment=payment)

@router.get("/payments/{payment_id}", response_model=PaymentResponse)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = get_payment(db=db, payment_id=payment_id)
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@router.delete("/payments/{payment_id}", response_model=dict)
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    return delete_payment_by_id(db=db, payment_id=payment_id)

@router.put("/payments/{payment_id}", response_model=PaymentResponse)
def update_payment_endpoint(payment_id: int, payment_data: PaymentCreate, db: Session = Depends(get_db)):
    return update_payment(db=db, payment_id=payment_id, payment_data=payment_data)