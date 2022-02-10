import json
import logging

from kafka.consumer import KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.producer import KafkaProducer

from config import settings

logger = logging.getLogger(__name__)


class KafkaWorker:
    def __init__(self):
        bootstrap_servers = f"{settings.KAFKA_SERVER}:{settings.KAFKA_PORT}"
        self._producer = KafkaProducer(bootstrap_servers=[bootstrap_servers])
        self._admin = KafkaAdminClient(bootstrap_servers=[bootstrap_servers])
        self.topic = None

    def create_topic(self, new_topic):
        topic = [NewTopic(new_topic, 1, 1)]
        self.topic = new_topic
        try:
            out = self._admin.create_topics(topic)
        except Exception as e:
            logger.error(f"Ошибка при создании топика {topic}: {repr(e)}")
        else:
            return out.succeeded

    def send_message(self, topic, key, value):
        key = str(key).encode('utf8')
        value = json.dumps(value).encode('utf8')
        try:
            self._producer.send(topic, key=key, value=value)
        except Exception as e:
            logger.error(f"Ошибка при добавлении сообщения: {repr(e)}")


class KafkaReceiver:
    def __init__(self):
        bootstrap_servers = f"{settings.KAFKA_SERVER}:{settings.KAFKA_PORT}"
        group_id = 'echo-messages-to-stdout'
        self._consumer = KafkaConsumer(bootstrap_servers=[bootstrap_servers], group_id=group_id,
                                       value_deserializer=lambda m: json.loads(m.decode('ascii')),)

    def consume(self, chunk_size, topics, timeout=20):
        self._consumer.subscribe(topics)
        messages = self._consumer.poll(max_records=chunk_size, timeout_ms=timeout)
        if messages:
            return messages.values()
