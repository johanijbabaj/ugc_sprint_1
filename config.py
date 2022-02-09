from pydantic import BaseSettings


class Settings(BaseSettings):
    # Настройки Kafka
    KAFKA_SERVER: str
    KAFKA_PORT: str


settings = Settings(_env_file=".env", _env_file_encoding="utf-8")
