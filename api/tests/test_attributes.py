import pytest

from flask import Flask
from typing import NamedTuple

from pynamodb.models import Model
from app.models.attributes import UnicodeDelimitedTupleAttribute

@pytest.fixture(scope = 'module', autouse=True)
def create_table():
    Mymodel.create_table()
class MyTuple(NamedTuple):
    name: str
    userid: str
class MyMeta(NamedTuple):
    prefix: str
    value: str
class Mymodel(Model):
    class Meta:
        host = 'http://localhost:8000'
        table_name = 'onething-pytest'
        read_capacity_units = 10
        write_capacity_units = 10

    PK = UnicodeDelimitedTupleAttribute(MyTuple, hash_key=True)
    SK = UnicodeDelimitedTupleAttribute(MyMeta, range_key=True)
    
def test_unicode_delimited_tuple_serialize():
    model = Mymodel()
    model.SK = MyMeta(prefix = 'Meta', value = '1234')
    model.PK = MyTuple(name = 'User', userid = '1234')
    print (model.SK)
    with pytest.raises(ValueError):
        model.save()