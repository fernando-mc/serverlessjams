def handler(event, context):
    print(event)
    print(context)
    # whole_auth_token should look like:
    # "Bearer SOME_CODE_GIBBERISH6r712fyasd"
    whole_auth_token = event.get('authorizationToken')
    print('Client token: ' + whole_auth_token)
    print('Method ARN: ' + event['methodArn'])
    if not whole_auth_token:
        raise Exception('Unauthorized')
    token_parts = whole_auth_token.split(' ')
    auth_token = token_parts[1]
    token_method = token_parts[0]
    if not (token_method.lower() == 'bearer' and auth_token):
        print("Failing due to invalid token_method or missing auth_token")
        raise Exception('Unauthorized')
    # At this point we've confirmed the token format looks ok
    # So it's time to validate the token to make sure it's authentic
    jsonurl = urlopen("https://"+AUTH0_DOMAIN+"/.well-known/jwks.json")
    jwks = json.loads(jsonurl.read())
    # This currently expects the token to have three distinct sections 
    # each separated by a period. Not sure how to get that with the
    # current token sent in from the frontend.
    unverified_header = jwt.get_unverified_header(token)
    try:
        auth0_id = jwt_verify(auth_token, AUTH0_CLIENT_PUBLIC_KEY)
        policy = generate_policy(auth0_id, 'Allow', event['methodArn'])
        return policy
    except Exception as e:
        print(f'Exception encountered: {e}')
        raise Exception('Unauthorized')

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
