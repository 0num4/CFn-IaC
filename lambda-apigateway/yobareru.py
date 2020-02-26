import json

def lambda_handler(event, context):
    # TODO implement
    print("---01: Payload:")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from L3ambda!')
    }
