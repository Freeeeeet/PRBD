from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserCreate, UserResponse
from app.crud import create_user, get_user, delete_user_by_id, update_user

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@router.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user_by_id(db=db, user_id=user_id)

@router.put("/users/{user_id}", response_model=UserResponse)
def update_user_endpoint(user_id: int, user_data: UserCreate, db: Session = Depends(get_db)):
    return update_user(db=db, user_id=user_id, user_data=user_data)