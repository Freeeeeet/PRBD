from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import InvoiceCreate, InvoiceResponse
from app.crud import create_invoice, get_invoice, delete_invoice_by_id, update_invoice

router = APIRouter()

@router.post("/invoices/", response_model=InvoiceResponse)
def create_invoice_endpoint(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    return create_invoice(db=db, invoice=invoice)

@router.get("/invoices/{invoice_id}", response_model=InvoiceResponse)
def read_invoice(invoice_id: int, db: Session = Depends(get_db)):
    invoice = get_invoice(db=db, invoice_id=invoice_id)
    if invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice

@router.delete("/invoices/{invoice_id}", response_model=dict)
def delete_invoice(invoice_id: int, db: Session = Depends(get_db)):
    return delete_invoice_by_id(db=db, invoice_id=invoice_id)

@router.put("/invoices/{invoice_id}", response_model=InvoiceResponse)
def update_invoice_endpoint(invoice_id: int, invoice_data: InvoiceCreate, db: Session = Depends(get_db)):
    return update_invoice(db=db, invoice_id=invoice_id, invoice_data=invoice_data)