from swagger_server.database.user import UserDataProvider
import time
import connexion
import six
from werkzeug.exceptions import Unauthorized

from jose import JWTError, jwt

# see https://github.com/zalando/connexion/tree/master/examples/openapi3/jwt

JWT_ISSUER = 'com.zalando.connexion'
JWT_SECRET = 'change_this'
JWT_LIFETIME_SECONDS = 600
JWT_ALGORITHM = 'HS256'


def generate_token(user_id):
    timestamp = _current_timestamp()
    payload = {
        "iss": JWT_ISSUER,
        "iat": int(timestamp),
        "exp": int(timestamp + JWT_LIFETIME_SECONDS),
        "sub": str(user_id),
    }

    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def get_secret(user, token_info) -> str:
    return '''
    You are user_id {user} and the secret is 'wbevuec'.
    Decoded token claims: {token_info}.
    '''.format(user=user, token_info=token_info)


def _current_timestamp() -> int:
    return int(time.time())


user_provider = UserDataProvider()


def signup():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = user_provider.user_exists(email) # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return False

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    user_provider.create_user(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    return True

def login():
    return generate_token(1)
