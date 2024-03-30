from sqlmodel import Field, SQLModel, Relationship

from model.public import Image, ShopImage
from services.utils import UtilService


class ItemBase(SQLModel):
    title: str = Field(index=True)
    price: int
    unity: str = Field(default="斤", nullable=False)
    description: str
    shop_uuid: str = Field(foreign_key="shop.uuid")


class Item(ItemBase, table=True):
    id: int = Field(primary_key=True)

    shop: "Shop" = Relationship(back_populates="items")
    images: "Image" = Relationship(back_populates="item")


class ItemOut(ItemBase):
    id: int
    shop: "Shop"
    images: Image | None = None


class ItemsOut(SQLModel):
    data: list[ItemOut]
    count: int


class Shop(SQLModel, table=True):
    id: int = Field(primary_key=True)
    uuid: str = Field(unique=True, index=True)
    name: str
    address: str
    opening_time: str
    closing_time: str

    # images: Mapped["Image"] = relationship(foreign_keys=[id], primaryjoin="Shop.id == Image.item_id")
    images: list["ShopImage"] = Relationship(back_populates="shop")
    items: list["Item"] = Relationship(back_populates="shop")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.uuid = UtilService.create_uuid()
