from tests.utils import create_jwt_token


def test__with_authenticated_user__returns_user_data(client, user):
    jwt = create_jwt_token(user)
    headers = {
        "Authorization": f"JWT {jwt}"
    }
    r = client.get(f"/users/me/", headers=headers)
    assert r.status_code == 200
    data = r.json()
    print(data)
    assert data['email'] == user.email
    assert data['name'] == user.name
    assert data['id'] == user.id
