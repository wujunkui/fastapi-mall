from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Relationship, Field

if TYPE_CHECKING:
    from .items import Item, Shop


class ImageBase(SQLModel):
    id: int = Field(primary_key=True)
    md5: str = Field(index=True, unique=True)
    url: str


class Image(ImageBase, table=True):
    item_id: int = Field(foreign_key="item.id")

    item: "Item" = Relationship(back_populates="images")


class ShopImage(ImageBase, table=True):
    __tablename__ = "shop_image"
    shop_id: int = Field(foreign_key="shop.id")
    shop: "Shop" = Relationship(back_populates="images")
