from pathlib import Path

from pydantic import ConfigDict
from pydantic_settings import BaseSettings

env_path = Path(__file__).parent.parent / Path(".env")


class Settings(BaseSettings):
    model_config = ConfigDict(env_file=env_path)

    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    @property
    def database_url(self):
        user = f"{self.DB_USER}:{self.DB_PASS}"
        database = f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return f"postgresql+psycopg2://{user}@{database}"


settings = Settings()
