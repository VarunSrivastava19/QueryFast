from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    client_url: str = ""
    sqlite_file: str = ""
    sqlite_url: str = f"sqlite:///{sqlite_file}"

settings = Settings()