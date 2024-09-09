import pytest
from django.contrib.auth.tokens import default_token_generator
import djoser.utils
import djoser.constants


def test__activates_user(client, user_factory):
    user = user_factory(is_active=False)
    assert user.is_active == False
    payload = {
        "uid": djoser.utils.encode_uid(user.pk),
        "token": default_token_generator.make_token(user)
    }
    r = client.post("/users/activation/", data=payload)
    assert r.status_code == 204
    user.refresh_from_db()
    assert user.is_active


@pytest.mark.parametrize("field, err_msg", [("uid", djoser.constants.Messages.INVALID_UID_ERROR), ("token",djoser.constants.Messages.INVALID_TOKEN_ERROR)])
def test__with_invalid_uid_or_token__returns_400(field, err_msg, client, user_factory):
    user = user_factory(is_active=False)
    assert user.is_active == False
    payload = {
        "uid": djoser.utils.encode_uid(user.pk),
        "token": default_token_generator.make_token(user)
    }
    payload[field] = "invalid_value"
    r = client.post("/users/activation/", data=payload)
    assert r.status_code == 400
    assert r.json()[field] == [err_msg]
    user.refresh_from_db()
    assert user.is_active == False
