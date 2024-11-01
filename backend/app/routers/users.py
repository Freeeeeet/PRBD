from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserCreateRequest, UserCreateResponse
from app.crud.users_crud import get_user_by_email, create_user

router = APIRouter()


@router.post("/register/", response_model=UserCreateResponse)
def register_user(user: UserCreateRequest, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db=db, email=user.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this e-mail already registered."
        )
    create_user(db=db, user=user)
    return {"success": True}


# @router.get("/users/{user_id}", response_model=UserResponse)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     user = get_user(db=db, user_id=user_id)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user
#
#
# @router.delete("/users/{user_id}", response_model=dict)
# def delete_user(user_id: int, db: Session = Depends(get_db)):
#     return delete_user_by_id(db=db, user_id=user_id)
#
#
# @router.put("/users/{user_id}", response_model=UserResponse)
# def update_user_endpoint(user_id: int, user_data: UserCreate, db: Session = Depends(get_db)):
#     return update_user(db=db, user_id=user_id, user_data=user_data)

