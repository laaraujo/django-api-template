# Happy path - 201
# Missing required fields - 400

import pytest
from tests.utils import faker
from users.models import User

def test__creates_user(client):
    password = faker.password()
    print(password)
    payload = {
        "email": faker.email(),
        "password": password,
        "re_password": password,
        "name": faker.name()
    }
    r = client.post("/users/", data=payload)
    assert r.status_code == 201
    data = r.json()
    user = User.objects.get(id=data["id"])
    assert data["name"] == user.name
    assert data["email"] == user.email


@pytest.mark.parametrize("field", ["email", "name", "password", "re_password"])
def test__with_missing_fields__returns_400(field, client):
    password = faker.password()
    payload = {
        "email": faker.email(),
        "password": password,
        "re_password": password,
        "name": faker.name()
    }
    del payload[field]
    r = client.post("/users/", data=payload)
    assert r.status_code == 400
    data = r.json()
    assert data[field] == ["This field is required."]



