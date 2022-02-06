from uuid import UUID

from models._base import OrjsonModel


class FilmBookmark(OrjsonModel):
    film_id: UUID
    user_id: UUID
    deleted: bool


class FilmRating(OrjsonModel):
    film_id: UUID
    user_id: UUID
    rating: float
    deleted: bool


class FilmProgress(OrjsonModel):
    film_id: UUID
    user_id: UUID
    sec: int
    watched: bool
