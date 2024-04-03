import hashlib
import aiofiles
from pathlib import Path
from loguru import logger

from fastapi import APIRouter, UploadFile, Depends
from sqlmodel import Session, select

from database import get_db_session
from model.public import Image

router = APIRouter()


@router.post("/images")
async def upload_image(file: UploadFile, item_id: int, db: Session = Depends(get_db_session)):
    content = await file.read()
    md5 = hashlib.md5(content).hexdigest()
    logger.debug(f"md5: {md5}")
    exist_file: Image = db.scalars(select(Image).where(Image.md5 == md5)).first()
    if not exist_file:
        file_suffix = file.filename.split(".")[-1]
        logger.debug(f"file suffix: {file_suffix}")
        file_new_name = f"{md5}.{file_suffix}"
        file_path_str = Path('..') / 'static/images/upload' / file_new_name
        async with aiofiles.open(file_path_str, "wb") as f:
            await f.write(content)
        image = Image(md5=md5, url=file_path_str, item_id=item_id)
        db.add(image)
        db.commit()
        db.refresh(image)
        exist_file = image
    return exist_file
