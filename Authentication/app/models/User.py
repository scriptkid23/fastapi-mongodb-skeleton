from app.db.events import instance
from umongo import Document,fields

@instance.register
class User(Document):
    name = fields.StringField()
    
    
