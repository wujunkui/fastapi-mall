from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import setting
from database import get_db_session
from schemas.user import UserCreate, UserLogin
from services.user import UserService
from services.utils import UtilService

router = APIRouter()


@router.get("/users")
async def get_current_user(token: str):
    db = get_db_session()
    token_data = UserService.get_user_by_token(token)
    if not token_data:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    return


@router.post("/users")
async def create_user(user: UserCreate, db: Session = Depends(get_db_session)):
    existing_user = UserService.get_user_by_email(user.email, db)
    if existing_user:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Email is already existing, please login")
    user = UserService.create_user(user, db)
    return user


@router.post("/login")
async def login(form: UserLogin, db: Session = Depends(get_db_session)):
    db_user = UserService.get_user_by_email(form.email, db)
    if not db_user:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="user is not registered")
    pwd_correct = UtilService.verify_password(form.password, db_user.hashed_password)
    if not pwd_correct:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="password is not correct")

    access_token_expires = timedelta(minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES)
    data = {"sub": db_user.email, "uuid": db_user.uuid}
    access_token = UtilService.create_access_token(data=data, expires_delta=access_token_expires)
    token_data = {"access_token": access_token, "token_type": "Bearer"}

    return {"token": token_data, "user": data}
