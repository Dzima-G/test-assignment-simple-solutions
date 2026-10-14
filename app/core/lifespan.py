from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import get_settings
from app.db.database import Database


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    settings = get_settings()
    database = Database(url=settings.db.url, echo=settings.debug)
    app.state.database = database

    try:
        yield
    finally:
        await database.dispose()
