from abc import ABC, abstractmethod
from typing import Optional

from fastapi import Depends
from kafka import KafkaProducer

kafka_producer: Optional[KafkaProducer] = None


def get_kafka() -> KafkaProducer:
    return kafka_producer


class AbstractStorage(ABC):
    @abstractmethod
    def send(self, topic, key, value):
        pass


class KafkaStorage(AbstractStorage):
    __conn: KafkaProducer

    def __init__(self, kafka_conn: Depends[get_kafka]):
        self.__conn = kafka_conn

    def send(self, some_topic, some_key, some_value):
        data = self.__conn.send(topic=some_topic, key=some_key, value=some_value)
        return data


def get_storage() -> AbstractStorage:
    kafka_producer = get_kafka()
    return KafkaStorage(kafka_producer)
