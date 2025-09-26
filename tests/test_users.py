import pytest

async def test_create_user_success(async_client):
    payload = {"name": "Alice", "email": "alice@example.com"}
    r = await async_client.post("/users", json=payload)
    assert r.status_code == 201
    body = r.json()
    assert body["id"] == 1
    assert body["name"] == "Alice"

async def test_get_user_success(async_client):
    create = await async_client.post("/users", json={"name":"Bob","email":"b@example.com"})
    uid = create.json()["id"]
    r = await async_client.get(f"/users/{uid}")
    assert r.status_code == 200
    assert r.json()["name"] == "Bob"

async def test_get_user_not_found(async_client):
    r = await async_client.get("/users/999")
    assert r.status_code == 404
    assert "not found" in r.json()["detail"].lower()

async def test_create_user_validation_error(async_client):
    r = await async_client.post("/users", json={"email":"no-name@example.com"})
    assert r.status_code == 422
    assert isinstance(r.json()["detail"], list)