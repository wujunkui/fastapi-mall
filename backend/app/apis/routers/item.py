from dataclasses import dataclass
from typing import Optional

from loguru import logger
from fastapi import APIRouter, Query, HTTPException
from fastapi import Depends
from sqlmodel import select, Session
from starlette import status

from database import get_db_session
from apis.deps import SessionDep
from model.items import Shop, Item
from schemas.items import ShopParam, ItemCreate

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
def create_shop(shop: ShopParam, db: SessionDep):
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
def update_shop(shop_uuid: str, shop: ShopParam, db: SessionDep):
    db_shop = db.exec(select(Shop).where(Shop.uuid == shop_uuid)).first()
    if not db_shop:
        raise HTTPException(detail="shop not found", status_code=404)

    update_dict = shop.model_dump(exclude_unset=True)
    db_shop.update(update_dict)
    db.add(db_shop)
    db.commit()
    db.refresh(db_shop)
    logger.debug(db_shop)
    return db


@router.delete("/shops/{shop_uuid}")
def delete_shop(shop_uuid: str, db: Session = Depends(get_db_session)):
    db_shop = db.scalars(select(Shop).where(Shop.uuid == shop_uuid)).first()
    db.delete(db_shop)
    db.commit()
    return {"detail": "shop deleted"}


@router.get("")
def get_items(page: PageParam, db: SessionDep, kw: str | None = None):
    stmt = select(Item).offset(page.offset).limit(page.size)
    if kw:
        stmt = stmt.where(Item.title.ilike(f"%{kw}%"))
    items = db.exec(stmt).all()
    return items


@router.post("/items")
def create_item(item: ItemCreate, db: SessionDep):
    shop = db.exec(select(Shop).where(Shop.uuid == item.shop_uuid)).first()
    if not shop:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="shop not found")
    db_item = db.exec(select(Item)
                      .where(Item.title == item.title, Item.shop_uuid == item.shop_uuid)).first()
    if db_item:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="item is already taken")
    db_item = Item(**item.model_dump(exclude_unset=True))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    logger.debug(db_item.shop)
    return db_item
