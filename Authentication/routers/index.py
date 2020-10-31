from fastapi import APIRouter

router = APIRouter()

@router.post("/api/v1/register")
async def login():
    return {"login" : "login"}