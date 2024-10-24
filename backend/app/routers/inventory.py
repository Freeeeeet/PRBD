from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import InventoryCreate, InventoryResponse
from app.crud import create_inventory, get_inventory, delete_inventory_item_by_id, update_inventory

router = APIRouter()

@router.post("/inventory/", response_model=InventoryResponse)
def create_inventory_item_endpoint(item: InventoryCreate, db: Session = Depends(get_db)):
    return create_inventory(db=db, item=item)

@router.get("/inventory/{item_id}", response_model=InventoryResponse)
def read_inventory_item(item_id: int, db: Session = Depends(get_db)):
    item = get_inventory(db=db, inventory_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return item

@router.delete("/inventory/{item_id}", response_model=dict)
def delete_inventory_item(item_id: int, db: Session = Depends(get_db)):
    return delete_inventory_item_by_id(db=db, item_id=item_id)

@router.put("/inventory/{item_id}", response_model=InventoryResponse)
def update_inventory_item(item_id: int, item_data: InventoryCreate, db: Session = Depends(get_db)):
    return update_inventory(db=db, item_id=item_id, inventory_data=item_data)