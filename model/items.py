from typing import List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column

from model import BaseModel
from model.public import Image


class Item(BaseModel):
    __tablename__ = 'item'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(index=True)
    price: Mapped[int]
    description: Mapped[str]
    shop_uuid: Mapped[str] = mapped_column(ForeignKey('shop.uuid'))

    shop: Mapped["Shop"] = relationship(back_populates="item")
    images: Mapped["Image"] = relationship(back_populates="item")

    # owner = relationship("User", back_populates="items")


class Shop(BaseModel):
    __tablename__ = "shop"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    uuid: Mapped[int] = mapped_column(unique=True, index=True)
    name: Mapped[str]
    address: Mapped[str]
    opening_time: Mapped[str]
    closing_time: Mapped[str]

    images: Mapped[List["Image"]] = relationship(back_populates="shop")
    items: Mapped[List["Item"]] = relationship(back_populates="shop")
