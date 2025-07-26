from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    client_url: str

settings = Settings()