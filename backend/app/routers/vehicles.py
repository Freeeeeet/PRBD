from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import VehicleCreate, VehicleResponse
from app.crud import create_vehicle, get_vehicle, delete_vehicle_by_id, update_vehicle

router = APIRouter()

@router.post("/vehicles/", response_model=VehicleResponse)
def create_vehicle_endpoint(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    return create_vehicle(db=db, vehicle=vehicle)

@router.get("/vehicles/{vehicle_id}", response_model=VehicleResponse)
def read_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle = get_vehicle(db=db, vehicle_id=vehicle_id)
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@router.delete("/vehicles/{vehicle_id}", response_model=dict)
def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    return delete_vehicle_by_id(db=db, vehicle_id=vehicle_id)

@router.put("/vehicles/{vehicle_id}", response_model=VehicleResponse)
def update_vehicle_endpoint(vehicle_id: int, vehicle_data: VehicleCreate, db: Session = Depends(get_db)):
    return update_vehicle(db=db, vehicle_id=vehicle_id, vehicle_data=vehicle_data)