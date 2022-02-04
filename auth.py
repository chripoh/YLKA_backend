import jwt

secrret_key = 'feY5QNYQVMItpPTWq8o7cZbgh9vxqlGuOOCA' #TODO: if public remove secret


def genAccessToken():
    # TODO Define needed Claims

    issuer = 'ylka.c-pohl.de'
    subject = 'the_user'
    audience = 'users'
    expiration = 'time???'
    issued_at = 'time_at_issue'

    payload = {
        'iss': issuer,
        'sub': subject,
        'aud': audience,
        'exp': expiration,
        'iat': issued_at
    }
    encoded_jwt = jwt.encode(payload, secrret_key, algorithm="HS256")

    return encoded_jwt


def genRefreshToken():
    # TODO: define Claims and Workflow for refreshing
    pass


def authToken():
    jwt.decode()
    pass

