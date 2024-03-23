from sqlalchemy import Integer, String, Column, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base


class Items(Base):
    __tablename__ = 'items'

    id: int = Column(Integer, primary_key=True)
    title: str = Column(String, index=True)
    description: str = Column(String)
    owner_uuid: str = Column(String, ForeignKey('users.uuid'))

    owner = relationship("User", back_populates="items")


class ItemImages(Base):
    __tablename__ = 'item_images'

    url: str = Column(String)
    item_id: int = Column(Integer, ForeignKey('items.id'))

    item = relationship("Item", back_populates="item_images")
