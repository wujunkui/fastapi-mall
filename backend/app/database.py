from collections.abc import Generator

from sqlmodel import Session, create_engine

from sqlalchemy.orm import sessionmaker

from setting import settings

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
