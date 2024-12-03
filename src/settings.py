from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class Settings(BaseSettings):
    """Pydantic settings class."""

    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: str
    docker_container_name: str

    model_config = SettingsConfigDict(env_file=".env.development")


if os.environ.get("RUN_ENV") == "test":
    settings = Settings(_env_file=".env.test")
else:
    settings = Settings()
