from pydantic import BaseModel


class ShopParam(BaseModel):
    name: str
    address: str
    opening_time: str
    closing_time: str
