import json
import logging
from abc import ABC, abstractmethod
from typing import Optional

from fastapi import Depends
from kafka import KafkaProducer

kafka_producer: Optional[KafkaProducer] = None

logger = logging.getLogger(__name__)


def get_kafka() -> KafkaProducer:
    return kafka_producer


class AbstractStorage(ABC):
    @abstractmethod
    def send(self, topic, key, value):
        pass


class KafkaStorage(AbstractStorage):
    __conn: KafkaProducer

    def __init__(self, kafka_conn: KafkaProducer = Depends(get_kafka)):
        self.__conn = kafka_conn

    def send_message(self, topic, key, value):
        try:
            self.__conn.send(topic, key=key, value=value)
        except Exception as e:
            logger.error(f"Ошибка при добавлении сообщения: {repr(e)}")
            return False
        else:
            return True


def get_storage() -> AbstractStorage:
    kafka_producer = get_kafka()
    return KafkaStorage(kafka_producer)
