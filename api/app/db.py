import boto3
class DynamoDb(object):
    
    def __init__(self, endpoint_url):
        self.con = None
        self.endpoint_url = endpoint_url
    def get_db(self):
        if not self.con:
            self.con = boto3.resource('dynamodb', endpoint_url=self.endpoint_url)
        return self.con
    