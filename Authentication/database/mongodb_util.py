import logging
from mongoengine import connect, disconnect
from core.config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT,MONGO_DB

async def connect_to_mongo():
    try:
        logging.info("Starting MongoDB connection...")
        
        connect(
            db= MONGO_DB,
            host= str(MONGODB_URL)
        )
        logging.info("Connect MongoDB succeeded.")
       
    except:
        logging.error("Connect to database failed！")


async def close_mongo_connection():
    try:
        logging.info("MongoDB disconnection...")
        disconnect()
    except:
        logging.info("MongoDB disconnect failed! ")