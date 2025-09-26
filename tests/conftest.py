import pytest
from httpx import AsyncClient
from app.main import app
from app import crud

@pytest.fixture(autouse=True)
def reset_data():
    crud.reset_db()

@pytest.fixture
async def async_client():
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client