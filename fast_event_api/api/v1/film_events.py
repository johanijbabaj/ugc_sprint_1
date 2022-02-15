"""
API для генерации событий при работе клиента с фильмами
"""

import logging
from http import HTTPStatus

from core.config import ErrorMessage
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer
from models.film_events import FilmBookmark, FilmProgress, FilmRating
from services.film_events import FilmEventsService, get_film_events_service

# Объект router, в котором регистрируем обработчики
router = APIRouter()
logger = logging.getLogger(__name__)
http_bearer = HTTPBearer()


@router.post("/bookmarks")
def bookmark_add(
    bookmark: FilmBookmark,
    film_events_service: FilmEventsService = Depends(get_film_events_service),
    token: bytes = Depends(http_bearer),
):
    """
    Метод для добавления фильма в закладки
    """

    result = film_events_service.post(bookmark, token)
    logger.info(result)
    if not result:
        raise HTTPException(
            status_code=HTTPStatus.SERVICE_UNAVAILABLE,
            detail=ErrorMessage.STORAGE_NOT_AVAILABLE,
        )
    return HTTPStatus.ACCEPTED


@router.post("/ratings")
def rating_add(
    rating: FilmRating,
    film_events_service: FilmEventsService = Depends(get_film_events_service),
    token: bytes = Depends(http_bearer),
):
    """
    Метод для установки рейтинга фильму
    """
    result = film_events_service.post(rating, token)
    logger.info(result)
    if not result:
        raise HTTPException(
            status_code=HTTPStatus.SERVICE_UNAVAILABLE,
            detail=ErrorMessage.STORAGE_NOT_AVAILABLE,
        )
    return HTTPStatus.ACCEPTED


@router.post("/progress")
def progress_add(
    progress: FilmProgress,
    film_events_service: FilmEventsService = Depends(get_film_events_service),
    token: bytes = Depends(http_bearer),
):
    """
    Метод для передачи прогресса просмотра фильма
    """
    result = film_events_service.post(progress, token)
    logger.info(result)
    if not result:
        raise HTTPException(
            status_code=HTTPStatus.SERVICE_UNAVAILABLE,
            detail=ErrorMessage.STORAGE_NOT_AVAILABLE,
        )
    return HTTPStatus.ACCEPTED
