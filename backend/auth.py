from get_token import get_token
from verify_token import verify_token

def handler(event, context):
    print(event)
    print(context)
    token = get_token(event)
    payload = verify_token(token)
    print(payload)
    if payload:
        policy = generate_policy("userfornow", 'Allow', event['methodArn'])
        return policy

def generate_policy(principal_id, effect, resource):
    return {
        'principalId': principal_id,
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": effect,
                    "Resource": resource

                }
            ]
        }
    }
