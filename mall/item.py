from dataclasses import dataclass
from typing import Optional

from loguru import logger
from fastapi import APIRouter, Query, HTTPException
from fastapi import Depends
from sqlalchemy import select
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
def get_shops(page: PageParam = Depends(), kw: Optional[str] = None, db: Session = Depends(get_db_session)):
    stmt = select(Shop).limit(page.size).offset(page.offset)
    if kw:
        stmt = stmt.where(Shop.name.ilike(f"%{kw}"))
    shops = db.scalars(stmt).all()
    return {"shops": shops}


@router.post("/shops")
def create_shop(shop: ShopParam, db: Session = Depends(get_db_session)):
    db_shop = db.scalars(select(Shop).where(Shop.name == shop.name)).first()
    if db_shop:
        raise HTTPException(detail="shop already exist", status_code=400)

    db_shop = Shop(name=shop.name, address=shop.address, opening_time=shop.opening_time, closing_time=shop.closing_time)
    db.add(db_shop)
    db.commit()
    db.refresh(db_shop)
    logger.debug(db_shop.items)
    logger.debug(db_shop.images)
    return db_shop


@router.get("/shops/{shop_uuid}")
async def get_shop_detail(shop_uuid: str, db: Session = Depends(get_db_session)):
    shop = db.scalars(select(Shop).where(Shop.uuid == shop_uuid)).first()
    return shop


@router.put("/shops/{shop_uuid}")
def update_shop(shop_uuid: str):
    pass


@router.delete("/shops/{shop_uuid}")
def delete_shop(shop_uuid: str, db: Session = Depends(get_db_session)):
    db_shop = db.scalars(select(Shop).where(Shop.uuid == shop_uuid)).first()
    db.delete(db_shop)
    db.commit()
    return {"detail": "shop deleted"}
