from abc import ABC, abstractmethod

from db.cache import MemoryCache


class AbstractService(ABC):

    CACHE_EXPIRE_IN_SECONDS = 60 * 60 * 24  # 24 часа

    name = None

    def __init__(self, cache: MemoryCache):
        self.cache = cache

    @abstractmethod
    def post(self):
        pass

    # def _get_key(self, *args):
    #     key = (self.name, args)
    #     return str(key)
