from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends, Query
from sqlmodel import Session

from database import get_db_session

SessionDep = Annotated[Session, Depends(get_db_session)]


@dataclass
class PageParam:
    page: int = Query(default=1, description="")
    size: int = Query(default=10)

    @property
    def offset(self):
        return (self.page - 1) * self.size


PageParamDep = Annotated[PageParam, Depends()]
