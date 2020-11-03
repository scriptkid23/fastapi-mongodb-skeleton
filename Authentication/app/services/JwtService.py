from datetime import datetime, timedelta
from typing import Dict

from jose import jwt
from pydantic import ValidationError

from app.models.schemas.Users import Users
from app.models.schemas.Jwt import JwtMeta, JwtUser
from app.core.config import(SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, JWT_SUBJECT)

# def create_jwt_token(
#     *,
#     jwt_content: Dict[str, str],
#     expires_delta: timedelta,
# ) -> str:
#     to_encode = jwt_content.copy()
#     expire = datetime.utcnow() + expires_delta
#     to_encode.update(JWTMeta(exp=expire, sub=JWT_SUBJECT).dict())
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM).decode()

# def create_access_token_for_user(user: Users) -> str:
#     return create_jwt_token(
#         jwt_content=JwtUser(username=user.username).dict(),
#         expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
#     )


