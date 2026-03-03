from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables / .env file."""

    DATABASE_URL: str
    SECRET_KEY: str = "change-me-to-a-random-secret-key"

    class Config:
        env_file = ".env"


settings = Settings()
