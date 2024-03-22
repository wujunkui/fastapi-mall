from sqlalchemy import Integer, String, Column, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base


class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String)
    owner_uuid = Column(String, ForeignKey('users.uuid'))

    owner = relationship("User", back_populates="items")


class ItemImages(Base):
    __tablename__ = 'item_images'

    url = Column(String)
    item_id = Column(Integer, ForeignKey('items.id'))

    item = relationship("Item", back_populates="item_images")
