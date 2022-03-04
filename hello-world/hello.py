import os
import json

# this function can be named anything, just make sure to supply it to the terraform instruction aws_lambda_function.handler
def handler(event, context):
    json_region = os.environ['AWS_REGION']
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps({
            "Region ": json_region,
            "message": "Hello, world!",
        }),
    }
