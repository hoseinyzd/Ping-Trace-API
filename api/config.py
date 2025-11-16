from pydantic import BaseSettings

class Settings(BaseSettings):
    ACCESS_TOKEN: str
    APP_USERNAME: str
    APP_PASSWORD: str
    ENVIRONMENT: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()
