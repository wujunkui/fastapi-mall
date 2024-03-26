from dataclasses import dataclass

from fastapi import APIRouter, Query
from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db_session

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
def create_shop():
    pass


@router.put("/shops/{shop_uuid}")
def update_shop(shop_uuid: str):
    pass


@router.delete("/shops/{shop_uuid}")
def delete_shop(shop_uuid: str):
    pass
