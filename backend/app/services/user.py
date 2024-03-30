import uuid
import logging
import setting

from fastapi import HTTPException
from sqlmodel import Session, col, select
from starlette import status
from jose import jwt, JWTError

from model.users import User
from schemas.user import UserCreate
from services.utils import UtilService


class UserService:

    @staticmethod
    def verify_token(token: str) -> bool:
        try:
            jwt.decode(token)
        except Exception as e:
            logging.warning(e)
            return False
        return True

    @staticmethod
    async def create_user(user: UserCreate, db: Session) -> User:
        hashed_password = UtilService.get_password_hash(user.password)
        db_user = User(email=user.email, hashed_password=hashed_password, uuid=uuid.uuid4().hex)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    async def get_user_by_email(email: str, db: Session) -> User | None:
        existing_user = db.exec(select(User).where(User.email == email)).first()
        return existing_user

    @staticmethod
    def get_user_by_token(token: str):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, setting.SECRET_KEY, algorithms=[setting.ALGORITHM])
            email: str = payload.get("sub")
            if not email:
                raise credentials_exception

        except JWTError:
            raise credentials_exception
        return payload
