from abc import ABC, abstractmethod
from typing import Optional

from fastapi import Depends

from redis import Redis

redis: Optional[Redis] = None


def get_redis() -> Optional[Redis]:
    return redis


class MemoryCache(ABC):
    @abstractmethod
    def set(self, key, data, expire):
        pass

    @abstractmethod
    def get(self, key):
        pass


class RedisCache(MemoryCache):
    __con = None

    def __init__(self, redis_instance: Depends[get_redis]):
        self.__con = redis_instance

    def set(self, key, data, expire):
        self.__con.set(key, data, expire=expire)

    def get(self, key):
        data = self.__con.get(key)
        return data


def get_cache() -> MemoryCache:
    redis_instance = get_redis()
    return RedisCache(redis_instance)
