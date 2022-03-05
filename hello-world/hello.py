import os
import json

# this function can be named anything, just make sure to supply it to the terraform instruction aws_lambda_function.handler
def handler(event, context):
    json_region = os.environ['AWS_REGION']
    if event['queryStringParameters'] is not None and event['queryStringParameters']['Name'] is not None:
        responseMessage = 'Hello, ' + event['queryStringParameters']['Name'] + '!';
    else:
        responseMessage = 'Hello, world!'
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': json.dumps({
            'Region ': json_region,
            'message': responseMessage,
        }),
    }
