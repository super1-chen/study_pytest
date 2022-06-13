import pytest
from sanic import Sanic
from sanic import response

@pytest.fixture
def app():
    sanic_app = Sanic(__name__)

    @sanic_app.get("/")
    async def basic(request):
        return response.text("foo")

    return sanic_app

@pytest.mark.asyncio
async def test_basic_asgi_client(app):
    request, response = await app.asgi_client.get("/")

    assert response.body == b"foo"
    assert response.status == 200