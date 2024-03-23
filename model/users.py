from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship

from ..database import Base


class User(Base):
    __tablename__ = "users"
    id: int = Column(Integer, autoincrement=True, primary_key=True)
    uuid: str = Column(String, unique=True, index=True)
    email: str = Column(String, unique=True, index=True)
    hashed_password: str = Column(String)
    is_active: bool = Column(Boolean, default=True)
