from pynamodb.models import Model
from flask import current_app
from pynamodb.attributes import UnicodeAttribute
def model_base_meta():
    class Meta:
        with current_app.app_context():
            host = current_app.config['DATABASE']
            table_name = current_app.config['DYNAMODB_TABLE']
            read_capacity_units = 1
            write_capacity_units = 1
    return Meta