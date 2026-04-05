from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    environment: Literal["development", "production", "testing"] = Field(
        "development",
        validation_alias="APP_ENV",
    )
    log_level: str = Field(
        "INFO",
        validation_alias="LOG_LEVEL",
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
