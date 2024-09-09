from django.core import mail


def test__resends_activation_email(client, user_factory):
    user = user_factory(is_active=False)
    r = client.post("/users/resend_activation/", data={"email": user.email})
    assert r.status_code == 204
    assert len(mail.outbox) == 1
    assert mail.outbox[0].to == [user.email]


def test__with_invalid_email__returns_400(client):
    r = client.post(
        "/users/resend_activation/", data={"email": "invalid_email@test.com"}
    )
    assert r.status_code == 400
    assert len(mail.outbox) == 0


def test__with_missing_email__returns_400(client):
    r = client.post("/users/resend_activation/")
    assert r.status_code == 400
    assert len(mail.outbox) == 0
    assert r.json()["email"] == ["This field is required."]
