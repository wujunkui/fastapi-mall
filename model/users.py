from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship

from model import BaseModel


class User(BaseModel):
    __tablename__ = "user"
    id = Column(Integer, autoincrement=True, primary_key=True)
    uuid = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
