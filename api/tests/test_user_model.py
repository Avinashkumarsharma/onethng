import pytest
def test_user_meta_create(client):
    from app.models.user import UserMeta
    meta = UserMeta("1234567")
    meta.first_name = "Avinash"
    meta.last_name = "Kumar"
    meta.save()

def test_user_meta_get(client):
    _id = '123456'
    from app.models.user import UserMeta, UserIdKey, UserMetaKey
    meta = UserMeta.get(UserIdKey(userid = _id), UserMetaKey(userid = _id))
    assert meta.first_name == 'Avinash'