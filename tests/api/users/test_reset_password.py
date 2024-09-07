from django.core import mail
from tests.utils import faker

def test__with_valid_email__sends_email(client, user):
    r = client.post("/users/reset_password/", data={"email": user.email})
    assert r.status_code == 204
    assert len(mail.outbox) == 1
    assert mail.outbox[0].to == [user.email]


def test__with_missing_email__returns_400(client, user):
    r = client.post("/users/reset_password/")
    assert r.status_code == 400
    assert len(mail.outbox) == 0
    data = r.json()
    assert data["email"] == ["This field is required."]


def test__with_invalid_email__returns_400(client):
    r = client.post("/users/reset_password/", data={"email": faker.email()})
    assert r.status_code == 400
    assert len(mail.outbox) == 0

