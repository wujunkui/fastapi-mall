from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase



class BaseModel(DeclarativeBase):
    __abstract__ = True


