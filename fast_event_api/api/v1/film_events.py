"""
Модели ответа API
"""

import logging
from http import HTTPStatus

from core.config import ErrorMessage
from fastapi import APIRouter, Depends, Header, HTTPException, Query, responses
from models.film_events import FilmBookmark, FilmProgress, FilmRating
from services.film_events import FilmEventsService, get_film_events_service
from utils import get_user_type

# Объект router, в котором регистрируем обработчики
router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/bookmarks")
def bookmark_add(
    bookmark: FilmBookmark,
    film_events_service: FilmEventsService = Depends(get_film_events_service),
):
    """
    Примеры обращений, которые должны обрабатываться API
    #GET /api/v1/bookmarks/
    """
    film_events_service.post(bookmark)
    # Если выборка пустая, отдаём 404 статус
    #raise HTTPException(
    #    status_code=HTTPStatus.NOT_FOUND, detail=ErrorMessage.FILM_NOT_FOUND
    #)
    return HTTPStatus.OK


