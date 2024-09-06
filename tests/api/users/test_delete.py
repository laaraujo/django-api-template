# Happy Path - 204
# Unauthenticated user - 401
# Not found - 404
# Unauthorized - 404 (Not 403, to avoid exposing data)

import pytest
from users.models import User


def test__with_auth_user__deletes_user(client, user_factory):
    pwd = 'test'
    user = user_factory(password=pwd)
    client.force_authenticate(user)
    r = client.delete(f"/users/{user.id}/", data={"current_password": pwd})
    assert r.status_code == 204
    with pytest.raises(User.DoesNotExist):
        assert user.refresh_from_db()

def test__with_diff_user__returns_403(client, user, user_factory):
    pwd = 'test'
    diff_user = user_factory(password=pwd)
    client.force_authenticate(user)
    r = client.delete(f"/users/{diff_user.id}/", data={"current_password": pwd})
    assert r.status_code == 403

def test__with_anonymous_user__returns_401(client, user_factory):
    pwd = 'test'
    user = user_factory(password=pwd)
    r = client.delete(f"/users/{user.id}/", data={"current_password": pwd})
    assert r.status_code == 401
