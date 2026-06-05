"""Application configuration settings.

This module defines the application's configuration using
pydantic-settings. Values are loaded from environment variables
and may be overridden through a .env file.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    ollama_base_url: str
    llm_model: str
    max_iterations: int
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
