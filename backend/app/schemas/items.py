from pydantic import BaseModel


class ShopParam(BaseModel):
    name: str
    address: str
    opening_time: str
    closing_time: str


class ItemCreate(BaseModel):
    title: str
    description: str | None = None
    price: int = 0
    unity: str = "斤"
    shop_uuid: str
