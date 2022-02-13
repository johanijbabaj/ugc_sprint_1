import logging
import uuid
from functools import lru_cache
from time import sleep, time

import jwt
import orjson
from db.cache import MemoryCache, get_cache
from db.storage import AbstractStorage, get_storage
from fastapi import Depends
from services.abstract import AbstractService

logger = logging.getLogger(__name__)


class FilmEventsService(AbstractService):
    """
    FilmEventsService содержит бизнес-логику по работе с событиями фильмов.
    """

    def __init__(self, *args, **kwargs):
        self.name = "film_events"
        super().__init__(*args, **kwargs)

    def post(self, message, token):
        logger.info(message)
        token_bytes = token.credentials.encode()
        #  Получаем user_id из токена
        decoded_payload = jwt.decode(token_bytes, options={"verify_signature": False})
        message.user_id = decoded_payload.get("sub")
        key = f"{message.user_id}{message.film_id}"
        event_message = message.toJSON()
        event_topic = message._topic
        result = self.storage.send(event_topic, key.encode(), event_message)
        if result:
            logger.info(f"Записано сообщение {event_message} в топик {event_topic}")
        return result


@lru_cache()
def get_film_events_service(
    cache: MemoryCache = Depends(get_cache),
    storage: AbstractStorage = Depends(get_storage),
) -> FilmEventsService:
    return FilmEventsService(cache, storage)
