import boto3
import argparse
parser = argparse.ArgumentParser(description='Data Setup Util')
def create_table(name, url):
    dynamodb = boto3.client('dynamodb', endpoint_url = url)
    try:
        dynamodb.create_table(
            TableName=name,
            AttributeDefinitions=[
                {
                    "AttributeName": "PK",
                    "AttributeType": "S"
                },
                {
                    "AttributeName": "SK",
                    "AttributeType": "S"
                }
            ],
            KeySchema=[
                {
                    "AttributeName": "PK",
                    "KeyType": "HASH"
                },
                {
                    "AttributeName": "SK",
                    "KeyType": "RANGE"
                }
            ],
            ProvisionedThroughput={
                "ReadCapacityUnits": 1,
                "WriteCapacityUnits": 1
            }
        )
    except Exception as e:
        print("Could not create table. Error:")
        print(e)
    print("TABLE CREATED")
if __name__ == '__main__':
    create_table('onething-dev', "http://localhost:8000")

