from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import get_settings
from app.core.lifespan import lifespan


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name, lifespan=lifespan)

    app.include_router(api_router, prefix="/api/v1")

    return app
