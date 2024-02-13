from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal


class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST", "PROD"]

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    POSTGRES_HOST: str
    POSTGRES_POST: int

    POSTGRES_DB_TEST: str
    POSTGRES_USER_TEST: str
    POSTGRES_PASSWORD_TEST: str
    POSTGRES_HOST_TEST: str
    POSTGRES_POST_TEST: int

    @property
    def DATABASE_URL(self):
        return f"postgresql+psycopg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_POST}/{self.POSTGRES_DB}"

    @property
    def DATABASE_URL_TEST(self):
        return f"postgresql+psycopg://{self.POSTGRES_USER_TEST}:{self.POSTGRES_PASSWORD_TEST}@{self.POSTGRES_HOST_TEST}:{self.POSTGRES_POST_TEST}/{self.POSTGRES_DB_TEST}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
