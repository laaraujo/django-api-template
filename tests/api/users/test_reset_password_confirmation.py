import pytest
from tests.utils import faker
from django.contrib.auth.tokens import default_token_generator
import djoser


def test__with_valid_uid_and_token__updates_password(client, user):
    pwd = faker.password()
    assert not user.check_password(pwd)

    payload = {
        "uid": djoser.utils.encode_uid(user.pk),
        "token": default_token_generator.make_token(user),
        "new_password": pwd,
        "re_new_password": pwd,
    }
    r = client.post("/users/reset_password_confirm/", data=payload)
    assert r.status_code == 204
    user.refresh_from_db()
    assert user.check_password(pwd)


@pytest.mark.parametrize("field", ["uid", "token", "new_password", "re_new_password"])
def test__with_missing_fields__returns_400(field, client, user):
    pwd = faker.password()
    assert not user.check_password(pwd)
    payload = {
        "uid": djoser.utils.encode_uid(user.pk),
        "token": default_token_generator.make_token(user),
        "new_password": pwd,
        "re_new_password": pwd,
    }
    del payload[field]
    r = client.post("/users/reset_password_confirm/", data=payload)
    assert r.status_code == 400
    data = r.json()
    assert data[field] == ["This field is required."]
    user.refresh_from_db()
    assert not user.check_password(pwd)


def test__with_invalid_uid__returns_400(client, user):
    pwd = faker.password()
    assert not user.check_password(pwd)

    payload = {
        "uid": "invalid_uid",
        "token": default_token_generator.make_token(user),
        "new_password": pwd,
        "re_new_password": pwd,
    }
    r = client.post("/users/reset_password_confirm/", data=payload)
    assert r.status_code == 400
    user.refresh_from_db()
    assert not user.check_password(pwd)


def test__with_invalid_token__returns_400(client, user):
    pwd = faker.password()
    assert not user.check_password(pwd)

    payload = {
        "uid": djoser.utils.encode_uid(user.pk),
        "token": "invalid_token",
        "new_password": pwd,
        "re_new_password": pwd,
    }
    r = client.post("/users/reset_password_confirm/", data=payload)
    assert r.status_code == 400
    user.refresh_from_db()
    assert not user.check_password(pwd)


def test__with_password_mismatch__returns_400(client, user):
    pwd = faker.password()
    assert not user.check_password(pwd)

    payload = {
        "uid": djoser.utils.encode_uid(user.pk),
        "token": default_token_generator.make_token(user),
        "new_password": pwd,
        "re_new_password": "different_password",
    }
    r = client.post("/users/reset_password_confirm/", data=payload)
    assert r.status_code == 400
    user.refresh_from_db()
    assert not user.check_password(pwd)
