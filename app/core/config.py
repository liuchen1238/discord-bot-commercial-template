"""Centralized application settings loaded from environment variables."""
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_env: str = "development"
    log_level: str = "INFO"
    secret_key: str = "change-me"
    maintenance_mode: bool = False

    discord_token: str = ""
    discord_client_id: str = ""
    discord_client_secret: str = ""
    discord_guild_id_dev: str = ""

    database_url: str = "sqlite+aiosqlite:///./dev.db"
    redis_url: str = "redis://localhost:6379/0"

    stripe_api_key: str = ""
    stripe_webhook_secret: str = ""
    stripe_price_id_pro: str = ""

    openai_api_key: str = ""
    github_token: str = ""

    api_host: str = "0.0.0.0"
    api_port: int = 8000


@lru_cache
def get_settings() -> Settings:
    return Settings()
