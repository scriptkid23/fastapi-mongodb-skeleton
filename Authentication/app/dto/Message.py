from pydantic import BaseModel

class Message(BaseModel):
    code: str
    message: str
    