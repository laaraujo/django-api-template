# Happy Path - 204
# Unauthenticated user - 401
# Not found - 404
# Unauthorized - 404 (Not 403, to avoid exposing data)

def test__with_auth_admin_user__deletes_user(client, user_factory):
    pwd = 'test'
    user = user_factory(password=pwd)
    client.force_authenticate(user)
    r = client.delete(f"/users/{user.id}/", data={"current_password": pwd})
    assert r.status_code == 204
    # data = r.json()
    # assert User.object.get
    # assert
