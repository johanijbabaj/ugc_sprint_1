from uuid import UUID

from models._base import OrjsonModel


class FilmBookmark(OrjsonModel):
    film_id: UUID
    user_id: UUID
    added: bool


# producer.send(
#     topic='bookmarks',
#     key=b'film_id+user_id',
#     value=b'{"added": True}',
# )


class FilmRating(OrjsonModel):
    film_id: UUID
    user_id: UUID
    rating: float
    deleted: bool


# producer.send(
#     topic='ratings',
#     key=b'film_id+user_id',
#     value=b'{"rating": 10, "deleted": False}',
# )


class FilmProgress(OrjsonModel):
    film_id: UUID
    user_id: UUID
    sec: int
    watched: bool


# producer.send(
#     topic='progress',
#     key=b'film_id+user_id',
#     value=b'{"sec": 2334, "watched": True}',
# )
