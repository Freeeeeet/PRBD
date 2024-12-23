from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.config import logger
from app import models, schemas
from app.utils.security import hash_password, verify_password, create_access_token


def create_user(db: Session, user: schemas.UserCreateRequest):
    try:
        password_hash = hash_password(user.password)
        db_user = models.User(
            name=user.name,
            email=user.email,
            password_hash=password_hash
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        logger.info(f"User {user.email} added to database correctly, returning user")
        return db_user
    except Exception as e:
        db.rollback()
        logger.error(f"An error occurred while adding user to DB. {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while adding user to the database."
        )


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.password_hash):
        return None
    return user


def create_token(db: Session, user_id: int):
    try:
        access_token = create_access_token()
        db_token = models.Token(
            user_id=user_id,
            token=access_token,
        )
        db.add(db_token)
        db.commit()
        db.refresh(db_token)
        logger.info(f"Token for user {user_id} added to database correctly, returning user")
        return db_token
    except Exception as e:
        db.rollback()
        logger.error(f"An error occurred while adding token to DB. {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while adding token to the database."
        )


def get_token(db: Session, user_id: int):
    try:
        token = db.query(models.Token).filter(models.Token.user_id == user_id).first()
        return token
    except Exception as e:
        logger.error(f"An error occurred while getting token from db for user {user_id}: {e}", exc_info=True)
        return None


def check_auth(db: Session, token: str):
    try:
        user = db.query(models.Token).filter(models.Token.token == token).first()
        return user
    except Exception as e:
        logger.error(f"An error occurred while checking user token: {e}", exc_info=True)
        return None
