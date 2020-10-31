from fastapi import APIRouter

from app.api.routes import demo


router = APIRouter()
router.include_router(demo.router, tags=["authentication"], prefix="/users")
