from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import ShipmentCreate, ShipmentResponse
from app.crud import create_shipment, get_shipment, delete_shipment_by_id, update_shipment

router = APIRouter()

@router.post("/shipments/", response_model=ShipmentResponse)
def create_shipment_endpoint(shipment: ShipmentCreate, db: Session = Depends(get_db)):
    return create_shipment(db=db, shipment=shipment)

@router.get("/shipments/{shipment_id}", response_model=ShipmentResponse)
def read_shipment(shipment_id: int, db: Session = Depends(get_db)):
    shipment = get_shipment(db=db, shipment_id=shipment_id)
    if shipment is None:
        raise HTTPException(status_code=404, detail="Shipment not found")
    return shipment

@router.delete("/shipments/{shipment_id}", response_model=dict)
def delete_shipment(shipment_id: int, db: Session = Depends(get_db)):
    return delete_shipment_by_id(db=db, shipment_id=shipment_id)

@router.put("/shipments/{shipment_id}", response_model=ShipmentResponse)
def update_shipment_endpoint(shipment_id: int, shipment_data: ShipmentCreate, db: Session = Depends(get_db)):
    return update_shipment(db=db, shipment_id=shipment_id, shipment_data=shipment_data)