import pytest
from sanic import Sanic
from sanic import response

@pytest.yield_fixture
def app():
    app = Sanic("test_sanic_app")

    @app.route("/test_get", methods=['GET'])
    async def test_get(request):
        return response.json({"GET": True})

    yield app

@pytest.fixture
def sanic_server(loop, app, test_server):
    return loop.run_until_complete(test_server(app))