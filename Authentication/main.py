from fastapi import FastAPI
from routers import index
from fastapi.staticfiles import StaticFiles
app = FastAPI()



app.include_router(index.router)