from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "NexusNotify"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    API_PREFIX: str = "/api/v1"

    DATABASE_URL: str

    OLLAMA_HOST: str | None = None
    LLM_PROVIDER: str
    GROQ_API_KEY: str
    LLM_MODEL: str
    EMBEDDING_MODEL: str

    DATASET_PATH: str

    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()