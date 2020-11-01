from fastapi import FastAPI
from loguru import logger
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from umongo import MotorAsyncIOInstance

from app.core.config import DATABASE_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT

instance = MotorAsyncIOInstance()

async def init_mongo(app: FastAPI,mongodb_uri: str, minPoolSize: int, maxPoolSize: int):
    logger.info(f'Init Mongo')
    loop = asyncio.get_event_loop()
    conn = AsyncIOMotorClient(mongodb_uri, io_loop=loop,minPoolSize = minPoolSize, maxPoolSize = maxPoolSize)
    return conn.get_database('service-box')

async def connect_to_db(app: FastAPI) -> None:
    logger.info("Connecting to {0}", repr(DATABASE_URL))
    
    app.state.pool = await init_mongo(
        app,
        str(DATABASE_URL),
        minPoolSize=MIN_CONNECTIONS_COUNT,
        maxPoolSize=MAX_CONNECTIONS_COUNT
    )
    logger.info(await app.state.pool['user'].find_one({"name" : "123"}))
    instance.init(app.state.pool)
    
    logger.info("Connection established")


async def close_db_connection(app: FastAPI) -> None:
    logger.info("Closing connection to database")

    app.state.pool.client.close()

    logger.info("Connection closed")
