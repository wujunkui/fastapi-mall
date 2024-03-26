from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from model import BaseModel


class Image(BaseModel):
    __tablename__ = 'image'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    md5: Mapped[str] = mapped_column(index=True, unique=True)
    url: Mapped[str]
    item_id: Mapped[int]

    # item: Mapped[Item] = relationship(back_populates="item_images")
