from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    DATABASE_URL: str
    OLLAMA_BASE_URL: str
    OLLAMA_API_KEY: str
    OPENAI_DOMAIN_KEY: Optional[str] = None
    PORT: int = 8000
    DEBUG: bool = False
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-this-in-production")

    model_config = {"env_file": ".env", "extra": "ignore"}


settings = Settings()