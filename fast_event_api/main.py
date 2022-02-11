import logging

import uvicorn
from api.v1 import film_events
from core import config
from core.logger import LOGGING
from db import cache, storage
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from kafka import KafkaProducer

import redis
from redis import Redis

logger = logging.getLogger(__name__)
app = FastAPI(
    title=config.PROJECT_NAME,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)


@app.on_event("startup")
def startup():
    cache.redis = Redis(
        (config.REDIS_HOST, config.REDIS_PORT), password=config.REDIS_AUTH
    )
    logger.info(f"Kafka connection broker : {config.KAFKA_HOST}:{config.KAFKA_PORT}")
    storage.kafka_producer = KafkaProducer(
       bootstrap_servers=[f"{config.KAFKA_HOST}:{config.KAFKA_PORT}"]
    )


@app.on_event("shutdown")
def shutdown():
    cache.redis.close()
    storage.kafka_producer.close()


app.include_router(
    film_events.router, prefix="/api/v1/film_events", tags=["film_events"]
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_config=LOGGING,
        log_level=logging.DEBUG,
    )
