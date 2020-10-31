from fastapi import FastAPI
from routers import index
from fastapi.staticfiles import StaticFiles
app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(index.router)