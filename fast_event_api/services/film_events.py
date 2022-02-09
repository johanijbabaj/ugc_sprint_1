import logging
from functools import lru_cache

from db.cache import MemoryCache, get_cache
from db.storage import AbstractStorage, get_storage

from fastapi import Depends
from models.film_events import FilmBookmark, FilmProgress, FilmRating
from services.abstract import AbstractService
from time import time, sleep

logger = logging.getLogger(__name__)

class FilmEventsService(AbstractService):
    """
    FilmEventsService содержит бизнес-логику по работе с событиями фильмов.
    """

    def __init__(self, *args, **kwargs):
        self.name = "film_events"
        super().__init__(*args, **kwargs)

    def post(self, bookmark: FilmBookmark):
        logger.info(bookmark)
        curtime = time()
        logger.info(f"Время начала: {curtime}")
        for i in range(100000):
            hello, world = f"hello{i}", f"world{i}"
            self.storage.send("bookmarks", hello.encode("utf-8"), world.encode("utf-8"))
        curtimeend = time()
        logger.info(f"Время окончания: {curtimeend}"
                     f"Общеее время 100 000: {curtimeend-curtime}")


@lru_cache()
def get_film_events_service(
        cache: MemoryCache = Depends(get_cache),
        storage: AbstractStorage = Depends(get_storage),
) -> FilmEventsService:
    return FilmEventsService(cache, storage)
