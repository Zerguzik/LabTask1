from typing import Annotated

from sqlmodel import Session, SQLModel, create_engine
from fastapi import Depends

database_url = f"postgresql+psycopg2://postgres:qscesz@127.0.0.1/MainDB"
engine = create_engine(database_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# Зависимость сессии
def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
