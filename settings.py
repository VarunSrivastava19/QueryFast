from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    client_url: str = ""
    sqlite_file: str = ""

    model_config = SettingsConfigDict(env_file=".env", extra="allow")


settings = Settings()