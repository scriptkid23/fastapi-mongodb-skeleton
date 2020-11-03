from app.dto.Message import Message
from loguru import logger

from app.db.errors import EntityDoesNotExist
from app.dto.User import OutputSigninForm,InputSigninForm, InputSignupForm
from app.models.Users import Users
from .SecurityService import get_password_hash
async def signup(payload):
  
  newUser = Users(**payload.dict())
  newUser.password = get_password_hash(newUser.password)
  await newUser.ensure_indexes()
  await newUser.commit()

  
