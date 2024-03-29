from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from model import BaseModel


class Image(BaseModel):
    __tablename__ = 'image'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    md5: Mapped[str] = mapped_column(index=True, unique=True)
    url: Mapped[str]
    item_id: Mapped[int] = mapped_column(ForeignKey('item.id'))

    item: Mapped['Item'] = relationship(back_populates="images")


class ShopImage(BaseModel):
    __tablename__ = 'shop_image'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    md5: Mapped[str] = mapped_column(index=True, unique=True)
    url: Mapped[str]
    shop_id: Mapped[int] = mapped_column(ForeignKey('shop.id'))
    shop: Mapped['Shop'] = relationship(back_populates="images")
