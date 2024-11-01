from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import WarehouseCreate, WarehouseResponse
from app.crud.crud import create_warehouse, get_warehouse, delete_warehouse_by_id, update_warehouse

router = APIRouter()

@router.post("/warehouses/", response_model=WarehouseResponse)
def create_warehouse_endpoint(warehouse: WarehouseCreate, db: Session = Depends(get_db)):
    return create_warehouse(db=db, warehouse=warehouse)

@router.get("/warehouses/{warehouse_id}", response_model=WarehouseResponse)
def read_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    warehouse = get_warehouse(db=db, warehouse_id=warehouse_id)
    if warehouse is None:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    return warehouse

@router.delete("/warehouses/{warehouse_id}", response_model=dict)
def delete_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    return delete_warehouse_by_id(db=db, warehouse_id=warehouse_id)

@router.put("/warehouses/{warehouse_id}", response_model=WarehouseResponse)
def update_warehouse_endpoint(warehouse_id: int, warehouse_data: WarehouseCreate, db: Session = Depends(get_db)):
    return update_warehouse(db=db, warehouse_id=warehouse_id, warehouse_data=warehouse_data)