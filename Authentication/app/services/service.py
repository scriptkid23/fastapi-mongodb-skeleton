from app.models.User import User
from typing import AsyncIterable
async def find_users() -> AsyncIterable[User]:
    return User.find()
    