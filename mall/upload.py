import hashlib
import aiofiles
from pathlib import Path
from loguru import logger

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
    logger.debug(f"md5: {md5}")
    exist_file: ItemImage = db.scalars(select(ItemImage).where(ItemImage.md5 == md5)).first()
    if not exist_file:
        # todo insert into table
        file_suffix = file.filename.split(".")[-1]
        logger.debug(f"file suffix: {file_suffix}")
        file_new_name = f"{md5}.{file_suffix}"
        async with aiofiles.open(Path('.') / 'static/images/upload' / file_new_name, "wb") as f:
            await f.write(content)
        images = ItemImage(md5=md5)

    return exist_file
