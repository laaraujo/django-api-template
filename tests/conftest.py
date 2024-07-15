from collections.abc import Callable

import pytest
from model_bakery import baker
from rest_framework.test import APIClient
from users.models import User

from tests.utils import create_jwt_token, faker
from django.contrib.auth.hashers import make_password


def pytest_collection_modifyitems(items):
    """
    Add `pytest.mark.django_db()` mark to ALL tests.
    https://docs.pytest.org/en/latest/reference/reference.html#pytest.hookspec.pytest_collection_modifyitems
    """
    for item in items:
        item.add_marker("django_db")


@pytest.fixture
def client() -> APIClient:
    return APIClient()


@pytest.fixture
def user_factory() -> Callable[..., User]:
    def create_user(**kwargs) -> User:
        if 'password' in kwargs:
            kwargs['password'] = make_password(kwargs['password'])
        return baker.make(User, **kwargs)

    return create_user


@pytest.fixture
def user(user_factory: Callable[..., User]) -> User:
    return user_factory(is_active=True, is_admin=False)


@pytest.fixture
def jwt_token(user: User) -> str:
    return create_jwt_token(user)
