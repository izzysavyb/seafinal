import uuid
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

created_user_email = None
created_username = None

def test_register_user():
    global created_username, created_user_email

    created_username = f"user_{uuid.uuid4().hex[:8]}"
    created_user_email = f"{uuid.uuid4().hex[:8]}@test.com"

    response = client.post(
        "/auth/register",
        json={
            "username": created_username,
            "email": created_user_email,
            "password": "password123"
        }
    )

    assert response.status_code == 200

def test_register_duplicate_email():
    response = client.post(
        "/auth/register",
        json={
            "username": "anotheruser",
            "email": created_user_email,
            "password": "password123"
        }
    )

    assert response.status_code == 409


def test_login_success():
    response = client.post(
        "/auth/login",
        data={
            "username": created_username,
            "password": "password123"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_wrong_password():
    response = client.post(
        "/auth/login",
        data={
            "username": created_username,
            "password": "wrongpassword"
        }
    )

    assert response.status_code == 401


def test_login_nonexistent_user():
    response = client.post(
        "/auth/login",
        data={
            "username": "blaabalba",
            "password": "password123"
        }
    )

    assert response.status_code == 401


def test_register_short_password():
    response = client.post(
        "/auth/register",
        json={
            "username": "shortpass",
            "email": f"{uuid.uuid4()}@theitltd.com",
            "password": "123"
        }
    )

    assert response.status_code == 422


def test_register_invalid_email():
    response = client.post(
        "/auth/register",
        json={
            "username": "bademail",
            "email": "notanemail",
            "password": "password123"
        }
    )

    assert response.status_code == 422


def test_register_missing_username():
    response = client.post(
        "/auth/register",
        json={
            "email": f"{uuid.uuid4()}@theitltd.com",
            "password": "password123"
        }
    )

    assert response.status_code == 422


def test_login_missing_password():
    response = client.post(
        "/auth/login",
        data={
            "username": created_user_email
        }
    )

    assert response.status_code == 422


@pytest.mark.xfail
def test_intentional_fail_auth():
    response = client.post(
        "/auth/login",
        data={
            "username": created_user_email,
            "password": "password123"
        }
    )

    assert response.status_code == 401