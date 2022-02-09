from abc import ABC, abstractmethod

from db.cache import MemoryCache
from db.storage import AbstractStorage


class AbstractService(ABC):
    CACHE_EXPIRE_IN_SECONDS = 60 * 60 * 24  # 24 часа
    name = None

    def __init__(self, cache: MemoryCache, storage: AbstractStorage):
        self.cache = cache
        self.storage = storage

    @abstractmethod
    def post(self, *args):
        pass