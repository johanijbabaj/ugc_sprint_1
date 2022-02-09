import os
from logging import config as logging_config

from core.logger import LOGGING

# Применяем настройки логирования
logging_config.dictConfig(LOGGING)

# Название проекта. Используется в Swagger-документации
PROJECT_NAME = os.getenv("PROJECT_NAME", "movies_events")

# Настройки Redis
REDIS_HOST = os.getenv("REDIS_HOST", "0.0.0.0")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_AUTH = os.getenv("REDIS_AUTH", "password")


# Настройки Kafka
KAFKA_HOST = os.getenv("KAFKA_HOST", "kafka")
KAFKA_PORT = int(os.getenv("KAFKA_PORT", 9092))

# Корень проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Сообщения об ошибках
class ErrorMessage:
    FILM_NOT_FOUND = "Film(s) not found"
