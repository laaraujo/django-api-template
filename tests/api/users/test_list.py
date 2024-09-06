def test__with_auth_user__returns_same_user_only(client, user, user_factory):
    [user_factory() for _ in range(5)]
    client.force_authenticate(user)
    r = client.get("/users/")
    assert r.status_code == 200
    data = r.json()
    assert len(data["results"]) == 1
    assert data["results"][0] == {
        "email": user.email,
        "name": user.name,
        "id": user.id
    }

def test__with_auth_admin_user__returns_all_users(client, admin_user, user_factory):
    users = [user_factory() for _ in range(5)]
    client.force_authenticate(admin_user)
    r = client.get("/users/")
    assert r.status_code == 200
    data = r.json()
    assert len(data["results"]) == len(users) + 1


def test__with_anonymous_user__returns_401(client):
    r = client.get("/users/")
    assert r.status_code == 401
