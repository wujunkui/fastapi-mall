from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Item(Base):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(index=True)
    description: Mapped[str]
    owner_uuid: Mapped[str] = mapped_column(ForeignKey('users.uuid'))

    owner = relationship("User", back_populates="items")


class ItemImage(Base):
    __tablename__ = 'item_images'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    md5: Mapped[str] = mapped_column(String, index=True, unique=True)
    url: Mapped[str]
    item_id: Mapped[int] = mapped_column(ForeignKey('items.id'))

    item: Mapped[Item] = relationship(back_populates="item_images")
