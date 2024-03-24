import hashlib
from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db_session
from model.items import ItemImage

router = APIRouter()


@router.post("/images")
async def upload_image(file: UploadFile, db: Session = Depends(get_db_session)):
    content = await file.read()
    md5 = hashlib.md5(content).hexdigest()
    exist_file: ItemImage = db.scalars(select(ItemImage).where(ItemImage.md5 == md5)).first()
    if not exist_file:
        # todo insert into table
        pass

    return exist_file
