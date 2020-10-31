from fastapi import APIRouter, Body, Depends

router = APIRouter()

@router.get("/demo")
async def demo():
    return {"message":"demo"}