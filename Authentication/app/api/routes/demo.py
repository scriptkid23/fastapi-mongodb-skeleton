from fastapi import APIRouter, Body, Depends
from loguru import logger
from app.services.service import find_users
from typing import AsyncIterable, Dict
router = APIRouter()

@router.get("/demo")
async def demo():
    users = await find_users()
    # result = [item.dump() async for item in users]
    logger.info(users)
    async for item in users:
        print(item.dump())
    return "demo"