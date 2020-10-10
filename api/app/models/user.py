from app.models.model import BaseModel
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
class User(BaseModel):
    name = UnicodeAttribute(hash_key=True)
    