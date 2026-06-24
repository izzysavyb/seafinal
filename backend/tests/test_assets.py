from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def get_token():
    response = client.post(
        "/auth/login",
        data={
    "username": "admin",
    "password": "Admin123"
}
    )
    print(response.status_code)
    print(response.json())
    return response.json()["access_token"]


def test_create_asset():
    token = get_token()

    response = client.post(
        "/assets/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Test Laptop",
            "category": "Laptop",
            "serial_number": "TEST123",
            "status": "active"
        }
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Test Laptop"


def test_get_assets():
    token = get_token()

    response = client.get(
        "/assets/",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)