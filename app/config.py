from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DB_HOST: str
    DB_PORT: str
    DB_USER: st
    DB_PASS: str
    DB_NAME: str

    @property
    def database_url(self):
        user = f"{self.DB_USER}:{self.DB_PASS}"
        database = f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return f"postgresql+psycopg2://{user}@{database}"


settings = Settings()