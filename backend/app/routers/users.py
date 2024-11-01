from fastapi import APIRouter, Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas
from app.crud.users_crud import get_user_by_email, create_user, authenticate_user, create_token, get_token, check_auth
from app.config import logger
router = APIRouter()


@router.post("/create/", response_model=schemas.UserCreateResponse)
def create_user_endpoint(user: schemas.UserCreateRequest, token: str = Header(...), db: Session = Depends(get_db)):
    authed_user = check_auth(db=db, token=token)
    if not authed_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    existing_user = get_user_by_email(db=db, email=user.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this e-mail already registered."
        )
    create_user(db=db, user=user)
    logger.info(f"User {user.email} registered successfully")
    return {"success": True}


@router.post("/login", response_model=schemas.LoginUserResponse)
def login_user_endpoint(login_user: schemas.LoginUserRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db=db, email=login_user.email, password=login_user.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    token = get_token(db=db, user_id=user.id)
    if not token:
        token = create_token(db=db, user_id=user.id)

    logger.info(f"User {user.id} logged in successfully.")
    return {"token": f"{token.token}"}
