from datetime import datetime
from app.db.events import instance
from umongo import Document,fields

@instance.register
class JwtMeta(Document):
    exp = fields.DateTimeField(required=True)
    sub = fields.StringField(required=True)

@instance.register
class JwtUser(Document):
    username = fields.StringField(required=True)

