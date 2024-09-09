import pytest

from tests.utils import faker


def test__with_authenticated_user__changes_password(client, user_factory):
    pwd = faker.password()
    new_pwd = faker.password()
    assert new_pwd != pwd
    user = user_factory(password=pwd)
    client.force_authenticate(user)
    payload = {
        "current_password": pwd,
        "new_password": new_pwd,
        "re_new_password": new_pwd,
    }
    r = client.post("/users/set_password/", data=payload)
    assert r.status_code == 204
    user.refresh_from_db()
    assert user.check_password(new_pwd)


def test__with_anonymous_user__returns_400(client, user_factory):
    pwd = faker.password()
    new_pwd = faker.password()
    assert new_pwd != pwd
    user = user_factory(password=pwd)
    payload = {
        "current_password": pwd,
        "new_password": new_pwd,
        "re_new_password": new_pwd,
    }
    r = client.post("/users/set_password/", data=payload)
    assert r.status_code == 401
    user.refresh_from_db()
    assert user.check_password(new_pwd) == False


def test__with_incorrect_curr_password__returns_400(client, user_factory):
    pwd = faker.password()
    new_pwd = faker.password()
    assert new_pwd != pwd
    user = user_factory(password=pwd)
    client.force_authenticate(user)
    payload = {
        "current_password": "incorrect_password",
        "new_password": new_pwd,
        "re_new_password": new_pwd,
    }
    r = client.post("/users/set_password/", data=payload)
    assert r.status_code == 400
    user.refresh_from_db()
    assert user.check_password(new_pwd) == False


def test__with_different_re_new_password__returns_400(client, user_factory):
    pwd = faker.password()
    new_pwd = faker.password()
    assert new_pwd != pwd
    user = user_factory(password=pwd)
    client.force_authenticate(user)
    payload = {
        "current_password": pwd,
        "new_password": new_pwd,
        "re_new_password": "diff_re_new_password",
    }
    r = client.post("/users/set_password/", data=payload)
    assert r.status_code == 400
    user.refresh_from_db()
    assert user.check_password(new_pwd) == False


@pytest.mark.parametrize(
    "field", ["current_password", "new_password", "re_new_password"]
)
def test__with_missing_fields__returns_400(field, client, user_factory):
    pwd = faker.password()
    new_pwd = faker.password()
    assert new_pwd != pwd
    user = user_factory(password=pwd)
    client.force_authenticate(user)
    payload = {
        "current_password": pwd,
        "new_password": new_pwd,
        "re_new_password": new_pwd,
    }
    del payload[field]
    r = client.post("/users/set_password/", data=payload)
    assert r.status_code == 400
    data = r.json()
    assert data[field] == ["This field is required."]
    user.refresh_from_db()
    assert user.check_password(new_pwd) == False
