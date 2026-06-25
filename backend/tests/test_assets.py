import uuid

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

created_asset_id = None


def get_token():
    response = client.post(
        "/auth/login",
        data={
            "username": "testadmin",
            "password": "test1234"
        }
    )

    assert response.status_code == 200
    return response.json()["access_token"]


def auth_headers():
    token = get_token()
    return {"Authorization": f"Bearer {token}"}


# 1. Create asset
def test_create_asset():
    global created_asset_id
    unique_serial = str(uuid.uuid4())[:8]
    response = client.post(
        "/assets",
        json={
            "name": "Laptop",
            "category": "Electronics",
            "serial_number": unique_serial,
            "status": "active"
        },
        headers=auth_headers()
    )

    assert response.status_code == 200
    created_asset_id = response.json()["id"]


# 2. Get all assets
def test_get_assets():
    response = client.get(
        "/assets",
        headers=auth_headers()
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# 3. Get asset by ID
def test_get_asset_by_id():
    response = client.get(
        f"/assets/{created_asset_id}",
        headers=auth_headers()
    )

    assert response.status_code == 200
    assert response.json()["id"] == created_asset_id


# 4. Update asset name
def test_update_asset_name():
    response = client.put(
        f"/assets/{created_asset_id}",
        json={
            "name": "Updated Laptop"
        },
        headers=auth_headers()
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Updated Laptop"


# 5. Update asset status
def test_update_asset_status():
    response = client.put(
        f"/assets/{created_asset_id}",
        json={
            "status": "retired"
        },
        headers=auth_headers()
    )

    assert response.status_code == 200
    assert response.json()["status"] == "retired"


# 6. Update asset serial number
def test_update_asset_serial():
    response = client.put(
        f"/assets/{created_asset_id}",
        json={
            "serial_number": "XYZ999"
        },
        headers=auth_headers()
    )

    assert response.status_code == 200
    assert response.json()["serial_number"] == "XYZ999"


# 7. Search invalid asset (should 404)
def test_get_invalid_asset():
    response = client.get(
        "/assets/99999",
        headers=auth_headers()
    )

    assert response.status_code == 404


# 8. Create invalid asset (missing fields)
def test_create_invalid_asset():
    response = client.post(
        "/assets",
        json={
            "name": "Broken Asset"
        },
        headers=auth_headers()
    )

    assert response.status_code == 422


# 9. Delete asset
def test_delete_asset():
    response = client.delete(
        f"/assets/{created_asset_id}",
        headers=auth_headers()
    )

    assert response.status_code == 200


# 10. Intentional fail test
@pytest.mark.xfail
def test_intentional_fail():
    response = client.get(
        "/assets",
        headers=auth_headers()
    )

    # intentionally wrong
    assert response.status_code == 404