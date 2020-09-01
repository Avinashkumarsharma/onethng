from zappa.handler import LambdaHandler
def lambda_handler(event, context):
    return LambdaHandler.lambda_handler(event, context)