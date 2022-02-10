from kafka import KafkaProducer
from kafka import KafkaConsumer
from time import sleep
import json


producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda m: json.dumps(m).encode('ascii'))

producer.send(
    topic='movies_watch',
    value={
        "user_id": "700374cb-6be4-4732-bc0f-cdafe55735ce",
        "film_id": "de5676b0-40de-4ca8-9fdd-9e900d0e3eb7",
        "sec": 132,
        "watched": True}
)
sleep(1)

