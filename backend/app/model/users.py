from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    id: int = Field(primary_key=True)
    uuid: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    is_active: bool = Field(default=True)


class User(UserBase, table=True):
    hashed_password: str

