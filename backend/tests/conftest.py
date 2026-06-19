"""
Shared pytest fixtures for FinShield backend tests.

Environment variables are set BEFORE any app imports so that:
  - get_settings() lru_cache picks up test values on first call
  - APIKeyEncryptor gets a valid Fernet key at import time
  - SQLite is used — no external DB or Redis required
"""

import base64
import os

# ── Set test env vars before ANY app module is imported ──────────────────────
# Fernet requires URL-safe base64 of exactly 32 bytes.
_FERNET_KEY = base64.urlsafe_b64encode(b"test-key-for-pytest-only-32bytes").decode()
os.environ.setdefault("ENCRYPTION_KEY", _FERNET_KEY)
os.environ.setdefault("DATABASE_URL", "sqlite+aiosqlite:///./finshield_test.db")
os.environ.setdefault("APP_ENV", "development")  # triggers create_all_tables on startup
os.environ.setdefault("JWT_SECRET", "test-jwt-secret-finshield-pytest-ci")
os.environ.setdefault("REDIS_URL", "redis://localhost:6379/0")

# ── App imports (after env vars are in place) ─────────────────────────────────
import pytest  # noqa: E402
from httpx import AsyncClient, ASGITransport  # noqa: E402

from app.config import get_settings  # noqa: E402

# Clear cached settings so tests always use the env vars above.
get_settings.cache_clear()


@pytest.fixture
def anyio_backend():
    """Pin anyio-based async tests to asyncio.

    The app only ever runs under asyncio (uvicorn), and SQLAlchemy's async
    engine + aiosqlite is not driven correctly under trio, so running the
    trio backend produces spurious failures.
    """
    return "asyncio"


@pytest.fixture
async def client():
    """
    HTTP test client backed by an in-process SQLite database.

    httpx's ASGITransport does NOT run FastAPI lifespan events, so the
    schema is created explicitly here (the lifespan's create_all_tables()
    never fires under the test transport).  Importing create_app first
    registers every ORM model with Base.  Tables are dropped afterwards so
    each test starts from a clean database.
    """
    from app.main import create_app
    from app.db.session import create_all_tables, engine, Base

    application = create_app()
    await create_all_tables()
    try:
        async with AsyncClient(
            transport=ASGITransport(app=application),
            base_url="http://testserver",
        ) as ac:
            yield ac
    finally:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
