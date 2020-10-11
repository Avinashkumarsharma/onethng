import pytest
def test_user_meta_create(client):
    from app.models.user import UserMeta
    meta = UserMeta("1234567")
    meta.first_name = "Avinash"
    meta.last_name = "Kumar"
    meta.save()

def test_user_meta_get(client):
    _id = '123456'
    from app.models.user import UserMeta, UserKeyPK, UserMetaKey
    meta = UserMeta.get(UserKeyPK(uuid = _id), UserMetaKey(userid = _id))
    assert meta.first_name == 'Avinash'
def test_user_task_put(client):
    _id = '123456'
    from app.models.user import UserTask, UserTaskSK, UserKeyPK
    body = 'I will finish setting up this db by today'
    taskid = UserTaskSK(uid = _id, timestamp = 1234567890)
    task = UserTask(UserKeyPK(uuid = _id), taskid, body = body)
    task.save()
def test_user_task_get(client):
    _id = '123456'
    from app.models.user import UserTask, UserKeyPK, UserTaskSK
    tasksk = UserTaskSK(uid = _id, timestamp = 1234567890)
    task: UserTask = UserTask.get(UserKeyPK(uuid = _id), tasksk)
    assert len(task.body)