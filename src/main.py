from contextlib import asynccontextmanager

from fastapi import FastAPI
from users.users_endpoints import router as users_router
from core.db import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=users_router, prefix="/users")
