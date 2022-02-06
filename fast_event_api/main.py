import logging

import aioredis
import uvicorn
from api.v1 import film_events
from core import config
from core.logger import LOGGING
from db import cache, storage
from elasticsearch import AsyncElasticsearch
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

app = FastAPI(
    title=config.PROJECT_NAME,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


@app.on_event('startup')
async def startup():
    cache.redis = await aioredis.create_redis_pool((config.REDIS_HOST, config.REDIS_PORT), minsize=10,
                                                   maxsize=20, password=config.REDIS_AUTH)
    storage.es = AsyncElasticsearch(hosts=[f'{config.ELASTIC_HOST}:{config.ELASTIC_PORT}'])


@app.on_event('shutdown')
async def shutdown():
    await cache.redis.close()
    await storage.es.close()

app.include_router(film_events.router, prefix='/api/v1/film_events', tags=['film_events'])

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        log_config=LOGGING,
        log_level=logging.DEBUG,
    )
