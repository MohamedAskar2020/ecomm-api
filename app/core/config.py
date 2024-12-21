from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    # Database settings
    DATABASE_URL: str
    # .... other settings ...
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }




settings = Settings()
    


