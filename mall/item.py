from dataclasses import dataclass

from loguru import logger
from fastapi import APIRouter, Query
from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db_session
from model.items import Shop
from schemas.items import ShopParam

router = APIRouter()


@dataclass
class PageParam:
    page: int = Query(default=1, description="")
    size: int = Query(default=10)

    @property
    def offset(self):
        return (self.page - 1) * self.size


@router.get("/shops")
def get_shops(page: PageParam = Depends(), db: Session = Depends(get_db_session)):
    pass


@router.post("/shops")
def create_shop(shop: ShopParam, db: Session = Depends(get_db_session)):
    # todo check shop name repeat
    db_shop = Shop(name=shop.name, address=shop.address, opening_time=shop.opening_time, closing_time=shop.closing_time)
    db.add(db_shop)
    db.commit()
    db.refresh(db_shop)
    logger.debug(db_shop.items)
    logger.debug(db_shop.images)
    return db_shop


@router.put("/shops/{shop_uuid}")
def update_shop(shop_uuid: str):
    pass


@router.delete("/shops/{shop_uuid}")
def delete_shop(shop_uuid: str):
    pass
