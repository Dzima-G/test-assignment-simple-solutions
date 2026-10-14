from functools import lru_cache
from pathlib import Path

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

DOTENV_PATH = Path(__file__).resolve().parent / ".env"


class DBSettings(BaseModel):
    url: str = Field(
        default="postgresql+asyncpg://user:password@db:5432/name_db",
        description="DSN для соединения с PostgreSQL",
    )


class Settings(BaseSettings):
    app_name: str = "test-assignment-simple-solutions"
    debug: bool = False
    db: DBSettings = DBSettings()

    model_config = SettingsConfigDict(
        env_file=DOTENV_PATH,
        env_file_encoding="utf-8",
        extra="ignore",
        env_nested_delimiter="__",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
