import os
from logging import config as logging_config

from core.logger import LOGGING

# Применяем настройки логирования
logging_config.dictConfig(LOGGING)

# Название проекта. Используется в Swagger-документации
PROJECT_NAME = os.getenv('PROJECT_NAME', 'movies_events')

# Настройки Redis
REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_AUTH = os.getenv('REDIS_AUTH', "password")

# Корень проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Сообщения об ошибках
class ErrorMessage:
    FILM_NOT_FOUND = 'Film(s) not found'
