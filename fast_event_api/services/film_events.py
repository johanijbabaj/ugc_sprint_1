from functools import lru_cache
from typing import List, Optional

from db.cache import MemoryCache, get_cache
from fastapi import Depends
from models.film_events import FilmBookmark, FilmProgress, FilmRating
from services.abstract import AbstractService


class FilmEventsService(AbstractService):
    """
    FilmEventsService содержит бизнес-логику по работе с событиями фильмов.
    """

    def __init__(self, *args, **kwargs):
        self.name = "film_events"
        super().__init__(*args, **kwargs)

    # async def get_by_id(self, film_id: str) -> Optional[Film]:
    #
    #     film = await self._get_from_cache(film_id)
    #     if not film:
    #         film = await self._get_from_storage(film_id)
    #         if not film:
    #             return []
    #         # Сохраняем фильм в кеш
    #         await self._put_to_cache(film)
    #     return film
    #
    # async def _get_from_storage(self, film_id: str) -> Optional[Film]:
    #
    #     es_fields = [
    #         "id",
    #         "title",
    #         "imdb_rating",
    #         "description",
    #         "genres",
    #         "actors",
    #         "writers",
    #     ]
    #     doc = await self.storage.get("movies", film_id, es_fields)
    #     film_info = doc.get("_source")
    #     film_info["uuid"] = film_info["id"]
    #     film_info.pop("id")
    #     return Film(**film_info)
    def post(self):
        pass

    def _get_from_cache(self, key: str) -> Optional[FilmBookmark]:
        data = self.cache.get(key)
        if not data:
            return []
        return FilmBookmark.parse_raw(data)

    def _put_to_cache(self, key, bookmark: FilmBookmark):
        self.cache.set(str(key), bookmark.json(), expire=self.CACHE_EXPIRE_IN_SECONDS)


@lru_cache()
def get_film_events_service(
    cache: MemoryCache = Depends(get_cache),
) -> FilmEventsService:
    return FilmEventsService(cache)
