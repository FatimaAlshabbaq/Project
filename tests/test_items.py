async def test_create_item_success(async_client):
    payload = {"name":"Widget","price":9.99}
    r = await async_client.post("/items", json=payload)
    assert r.status_code == 201
    body = r.json()
    assert body["id"] == 1
    assert body["price"] == 9.99

async def test_get_item_success(async_client):
    create = await async_client.post("/items", json={"name":"Gadget","price":5.0})
    iid = create.json()["id"]
    r = await async_client.get(f"/items/{iid}")
    assert r.status_code == 200
    assert r.json()["name"] == "Gadget"

async def test_get_item_not_found(async_client):
    r = await async_client.get("/items/999")
    assert r.status_code == 404

async def test_list_items(async_client):
    await async_client.post("/items", json={"name":"A","price":1})
    await async_client.post("/items", json={"name":"B","price":2})
    r = await async_client.get("/items")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
    assert len(r.json()) == 2