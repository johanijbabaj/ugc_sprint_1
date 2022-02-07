import logging
from functools import lru_cache
from time import sleep, time

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

    def post(self, message):
        logger.info(message)
        curtime = time()
        logger.info(f"Время начала: {curtime}")
        key = str(message.user_id) + str(message.film_id)
        event_message = message.toJSON()
        result = self.storage.send(message._topic, key.encode(), event_message)
        if result:
            curtimeend = time()
            logger.info(
                f"Время окончания: {curtimeend}. Записано сообщение {event_message} в топик {message._topic}"
            )
        return result


@lru_cache()
def get_film_events_service(
    cache: MemoryCache = Depends(get_cache),
    storage: AbstractStorage = Depends(get_storage),
) -> FilmEventsService:
    return FilmEventsService(cache, storage)
