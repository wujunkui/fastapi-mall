from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from model import BaseModel

if TYPE_CHECKING:
    from .items import Item, Shop


class ImageBase(BaseModel):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    md5: Mapped[str] = mapped_column(index=True, unique=True)
    url: Mapped[str]


class Image(ImageBase):
    item_id: Mapped[int] = mapped_column(ForeignKey('item.id'))

    item: Mapped["Item"] = relationship(back_populates="images")


class ShopImage(ImageBase):
    __tablename__ = "shop_image"
    shop_id: Mapped[int] = mapped_column(ForeignKey("shop.id"))
    shop: Mapped["Shop"] = relationship(back_populates="images")
