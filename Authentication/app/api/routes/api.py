from fastapi import APIRouter

from app.api.routes import demo, Authentication

router = APIRouter()
router.include_router(demo.router, tags=["authentication"], prefix="/users")
router.include_router(Authentication.router, tags=["authentication"])