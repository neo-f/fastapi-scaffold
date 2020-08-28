import secrets
from typing import Optional

from pydantic import BaseSettings, HttpUrl, PostgresDsn


class Settings(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)

    SENTRY_DSN: Optional[HttpUrl] = None
    DATABASE_URI: Optional[PostgresDsn] = None

    class Config:
        case_sensitive = True


settings = Settings()
