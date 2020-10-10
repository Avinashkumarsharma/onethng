from pynamodb.models import Model
from flask import current_app
from pynamodb.attributes import UnicodeAttribute
class BaseModel(Model):
    class Meta:
        with current_app.app_context():
            table_name = current_app.config['DYNAMODB_TABLE']
        PK = UnicodeAttribute(hash_key=True)
        SK = UnicodeAttribute(range_key=True)