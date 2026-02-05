from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    chrome_binary: str | None = Field(default=None, alias="CHROME_BINARY")
    headless: bool = Field(default=False, alias="HEADLESS")
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

settings = Settings()