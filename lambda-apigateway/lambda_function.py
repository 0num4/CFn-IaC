import json

def lambda_handler(event, context):
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
