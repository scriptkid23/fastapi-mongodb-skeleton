import os
from starlette.datastructures import CommaSeparatedStrings, Secret
from databases import DatabaseURL
import logging

API_V1_STR = "/api"

JWT_TOKEN_PREFIX = "Token"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # one week



MAX_CONNECTIONS_COUNT = int(10)
MIN_CONNECTIONS_COUNT = int(3)
SECRET_KEY = Secret("123456")

PROJECT_NAME = "FastAPI example application"
ALLOWED_HOSTS = CommaSeparatedStrings("localhost")



MONGO_HOST = "object-information.i7udl.mongodb.net"
MONGO_USER = "alook"
MONGO_PASS = "alook12345678"
MONGO_DB = 'tip-tip-tap'
MONGODB_URL = DatabaseURL(
    f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}/{MONGO_DB}?retryWrites=true&w=majority"
)


database_name = MONGO_DB
article_collection_name = "articles"
favorites_collection_name = "favorites"
tags_collection_name = "tags"
users_collection_name = "users"
comments_collection_name = "commentaries"
followers_collection_name = "followers"

logging.basicConfig(format='%(levelname)-3s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG)