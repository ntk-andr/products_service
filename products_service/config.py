from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    
    POSTGRES_HOST: str
    POSTGRES_POST: int
    
    @property
    def DATABASE_URL(self):
        return f"postgresql+psycopg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_POST}/{self.POSTGRES_DB}"
    
    model_config = SettingsConfigDict(env_file=".env")
    
settings = Settings()