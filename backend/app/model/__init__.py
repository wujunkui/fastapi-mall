from sqlalchemy.orm import DeclarativeBase, declared_attr


class BaseModel(DeclarativeBase):
    __abstract__ = True
    __tablename__: str

    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def update(self, data: dict):
        for key, value in data.items():
            self.__setattr__(key, value)
        return self

    class Config:
        from_attributes = True
