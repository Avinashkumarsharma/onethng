from app.models.model import model_base_meta
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.models import Model
from .attributes import UnicodeDelimitedTupleAttribute
from typing import NamedTuple, Optional
class UserIdKey(NamedTuple):
    prefix: Optional[str] = "User"
    userid: Optional[str] = None
class UserMetaKey(NamedTuple):
    prefix: str = "Meta"
    userid: Optional[str] = None

class User(Model):
    PK = UnicodeDelimitedTupleAttribute(UserIdKey, hash_key=True)

class UserMeta(User):
    Meta = model_base_meta()
    def __init__(self, hash_key : Optional[str] = None, range_key: Optional[str] = None, _user_instantiated: Optional[bool] = True, **attributes) -> None:
        _hash_key = UserIdKey(userid = hash_key)
        _range_key = UserMetaKey(userid = hash_key)
        super(UserMeta, self).__init__(hash_key = _hash_key, range_key = _range_key, _user_instantiated = _user_instantiated, **attributes)

    SK = UnicodeDelimitedTupleAttribute(UserMetaKey, range_key = True)
    first_name = UnicodeAttribute()
    last_name = UnicodeAttribute()