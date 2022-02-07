import datetime
from abc import ABC
from uuid import UUID

from models._base import OrjsonModel


class FilmActions(ABC, OrjsonModel):
    film_id: UUID
    user_id: UUID
    _topic: str
    _created_at: datetime.datetime = datetime.datetime.utcnow()


class FilmBookmark(FilmActions):
    added: bool = True
    _topic = "bookmarks"


class FilmRating(FilmActions):
    rating: float
    deleted: bool = False
    _topic = "ratings"


class FilmProgress(FilmActions):
    sec: int
    watched: bool = False
    _topic = "progress"
