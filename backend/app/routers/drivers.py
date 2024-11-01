from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import DriverCreate, DriverResponse
from app.crud.crud import create_driver, get_driver, delete_driver_by_id, update_driver

router = APIRouter()

@router.post("/drivers/", response_model=DriverResponse)
def create_driver_endpoint(driver: DriverCreate, db: Session = Depends(get_db)):
    return create_driver(db=db, driver=driver)

@router.get("/drivers/{driver_id}", response_model=DriverResponse)
def read_driver(driver_id: int, db: Session = Depends(get_db)):
    driver = get_driver(db=db, driver_id=driver_id)
    if driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver

@router.delete("/drivers/{driver_id}", response_model=dict)
def delete_driver(driver_id: int, db: Session = Depends(get_db)):
    return delete_driver_by_id(db=db, driver_id=driver_id)

@router.put("/drivers/{driver_id}", response_model=DriverResponse)
def update_driver_endpoint(driver_id: int, driver_data: DriverCreate, db: Session = Depends(get_db)):
    return update_driver(db=db, driver_id=driver_id, driver_data=driver_data)