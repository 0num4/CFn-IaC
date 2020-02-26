import json
import boto3

def lambda_handler(event, context):
    # invoke lmabda
    client = boto3.client('lambda')
    
    # query = {
    # "test1": "test",
    # "test2": "test"
    # }
    print("---04: Payload:")
        #Lambdaを実行
    response = client.invoke(
        FunctionName='yobareru',
        InvocationType='RequestResponse',
        LogType='Tail'
        # Payload= query
    )
    
    #レスポンスを読む
    res = response['Payload'].read()
    print("---05: Payload:",res)
    # TODO implement
    mock = {
      "words": [
        {
          "sentence_index": 0,
          "begin": 0,
          "end": 1,
          "rubies": [
            {
              "partial_rubies": [
                {
                  "begin": 0,
                  "end": 1,
                  "surface": "角",
                  "ruby": "すみ",
                  "is_first": True
                }
              ],
              "is_first": True
            }
          ]
        }
      ]
    }
    return {
        'statusCode': 200,
        'body': json.dumps(mock)
    }
