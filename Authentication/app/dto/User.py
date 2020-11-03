from pydantic import BaseModel, EmailStr
from .RWSchema import RWSchema

class InputSignupForm(BaseModel):
    username: str
    email: EmailStr
    password: str
    

class InputSigninForm(BaseModel):
    email: EmailStr
    password: str

class OutputSigninForm(RWSchema):
    email: EmailStr
    image: str

class OutputSignupForm(RWSchema):
    pass



