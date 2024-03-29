from pydantic import BaseModel, EmailStr, validator


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserLogin(UserBase):
    password: str


class UserInfo(UserBase):
    is_active: bool


class User(UserBase):
    id: int
    uuid: str
    is_active: bool

    class Config:
        from_attributes = True
