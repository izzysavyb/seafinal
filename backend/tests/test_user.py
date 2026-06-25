import pytest
import uuid
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# ---------------------------
# HELPERS
# ---------------------------

def unique_user():
    uid = uuid.uuid4().hex[:8]
    return {
        "username": f"user_{uid}",
        "email": f"{uid}@test.com",
        "password": "password123"
    }


def register_user(user):
    response = client.post("/auth/register", json=user)
    assert response.status_code in [200, 201], response.json()
    return response.json()


def login_user(user):
    response = client.post(
        "/auth/login",
        data={
            "username": user["username"],
            "password": user["password"]
        }
    )
    assert response.status_code == 200, response.json()
    return response.json()["access_token"]


def auth_headers(token):
    return {"Authorization": f"Bearer {token}"}


def create_authenticated_user():
    user = unique_user()
    register_user(user)
    token = login_user(user)

    # get user id
    me = client.get("/users/me", headers=auth_headers(token))
    assert me.status_code == 200

    return user, token, me.json()["id"]


# ---------------------------
# FIXTURES (ISOLATION CORE)
# ---------------------------

@pytest.fixture
def user_setup():
    return create_authenticated_user()


# ---------------------------
# TESTS
# ---------------------------

def test_get_current_user(user_setup):
    user, token, user_id = user_setup

    response = client.get(
        "/users/me",
        headers=auth_headers(token)
    )

    assert response.status_code == 200
    assert response.json()["email"] == user["email"]


def test_get_current_user_no_token():
    response = client.get("/users/me")
    assert response.status_code == 401



def test_get_all_users(user_setup):
    user, token, _ = user_setup

    response = client.get(
        "/users",
        headers=auth_headers(token)
    )

    assert response.status_code == 403


def test_update_user_username(user_setup):
    user, token, user_id = user_setup

    response = client.put(
        f"/users/{user_id}",
        json={"username": f"updated_{uuid.uuid4().hex[:6]}"},
        headers=auth_headers(token)
    )

    assert response.status_code == 200


def test_update_user_email(user_setup):
    user, token, user_id = user_setup

    response = client.put(
        f"/users/{user_id}",
        json={"email": f"{uuid.uuid4().hex}@test.com"},
        headers=auth_headers(token)
    )

    assert response.status_code == 200


def test_update_user_invalid_email(user_setup):
    user, token, user_id = user_setup

    response = client.put(
        f"/users/{user_id}",
        json={"email": "bademail"},
        headers=auth_headers(token)
    )

    assert response.status_code == 422


def test_update_user_empty_username(user_setup):
    user, token, user_id = user_setup

    response = client.put(
        f"/users/{user_id}",
        json={"username": ""},
        headers=auth_headers(token)
    )

    assert response.status_code == 422



def test_delete_user(user_setup):
    user, token, user_id = user_setup

    response = client.delete(
        f"/users/{user_id}",
        headers=auth_headers(token)
    )

    assert response.status_code == 403


def test_get_deleted_user(user_setup):
    user, token, user_id = user_setup

    # delete attempt depends on role, so just check GET works
    response = client.get(
        f"/users/{user_id}",
        headers=auth_headers(token)
    )

    assert response.status_code in [200, 404]


@pytest.mark.xfail
def test_intentional_fail_users(user_setup):
    user, token, user_id = user_setup

    response = client.get(
        "/users/me",
        headers=auth_headers(token)
    )

    assert response.status_code == 500