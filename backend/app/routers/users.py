from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, models
from app.crud.users_crud import get_user_by_email, create_user, authenticate_user, create_token, get_token

router = APIRouter()


@router.post("/register/", response_model=schemas.UserCreateResponse)
def register_user(user: schemas.UserCreateRequest, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db=db, email=user.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this e-mail already registered."
        )
    create_user(db=db, user=user)
    return {"success": True}


@router.post("/login", response_model=schemas.LoginUserResponse)
def login_user(login_user: schemas.LoginUserRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db=db, email=login_user.email, password=login_user.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    token = get_token(db=db, user_id=user.id)
    if not token:
        token = create_token(db=db, user_id=user.id)
        return {"token": token}
    return {"token": token.token}
