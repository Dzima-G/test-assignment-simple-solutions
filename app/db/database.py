from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


class Database:
    """Управляет подключением к DB: engine и фабрика сессий."""

    def __init__(self, url: str, echo: bool = False) -> None:
        self._engine = create_async_engine(url, echo=echo, pool_pre_ping=True)
        self._session_factory = async_sessionmaker(self._engine, expire_on_commit=False)

    @asynccontextmanager
    async def session(self) -> AsyncGenerator[AsyncSession, None]:
        """Получает async DB session."""
        async with self._session_factory() as session:
            yield session

    async def dispose(self) -> None:
        """Корректно закрывает соединения при завершении работы."""
        await self._engine.dispose()
