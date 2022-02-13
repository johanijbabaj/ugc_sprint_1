"""
API для генерации событий при работе клиента с фильмами
"""

import logging
from http import HTTPStatus

from core.config import ErrorMessage
from fastapi import APIRouter, Depends, Header, HTTPException, Query, responses
from fastapi.security import OAuth2PasswordBearer
from models.film_events import FilmBookmark, FilmProgress, FilmRating
from services.film_events import FilmEventsService, get_film_events_service

# Объект router, в котором регистрируем обработчики
router = APIRouter()
logger = logging.getLogger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/bookmarks")
def bookmark_add(
    bookmark: FilmBookmark,
    film_events_service: FilmEventsService = Depends(get_film_events_service),
    token: str = Depends(oauth2_scheme),
):
    """
    Метод для добавления фильма в закладки
    """

    result = film_events_service.post(bookmark)
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
):
    """
    Метод для установки рейтинга фильму
    """
    result = film_events_service.post(rating)
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
):
    """
    Метод для передачи прогресса просмотра фильма
    """
    result = film_events_service.post(progress)
    logger.info(result)
    if not result:
        raise HTTPException(
            status_code=HTTPStatus.SERVICE_UNAVAILABLE,
            detail=ErrorMessage.STORAGE_NOT_AVAILABLE,
        )
    return HTTPStatus.ACCEPTED
