from faker import Faker
from rest_framework_simplejwt.tokens import AccessToken
from users.models import User

faker = Faker()


def create_jwt_token(user: User) -> str:
    token = AccessToken.for_user(user)
    return str(token)
