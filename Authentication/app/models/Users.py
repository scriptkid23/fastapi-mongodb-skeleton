from app.db.events import instance
from umongo import Document,fields

@instance.register
class Users(Document):
    username = fields.StringField(required=True)
    email = fields.EmailField(required=True,unique=True)
    hashed_password = fields.StringField(required=True)
    bio   = fields.StringField(required=True, default="")
    image = fields.StringField(default="https://storage-3t.herokuapp.com/uploads/avatar/001-unicorn.svg")
    disabled = fields.BooleanField(default=False)

    
