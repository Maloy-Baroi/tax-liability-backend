import jwt
from django.conf import settings


def get_user_id_from_jwt(token, algorithm='HS256'):
    secret_key = settings.SECRET_KEY

    try:
        decoded_token = jwt.decode(token, secret_key, algorithms=[algorithm])
        user_id = decoded_token.get('user_id')
        if user_id:
            return user_id
        else:
            return "User ID not found in the token."
    except jwt.ExpiredSignatureError:
        return "Token has expired."
    except jwt.InvalidTokenError:
        return "Invalid token."
