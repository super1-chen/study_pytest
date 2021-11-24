import pytest
from sanic import Sanic
from sanic import response
from sanic.websocket import WebSocketProtocol

@pytest.fixture
def app():
    app = Sanic("test_sanic_app", register=False)

    @app.route("/test_get", methods=['GET'])
    async def test_get(request):
        return response.json({"GET": True})

    @app.route("/test_post", methods=['POST'])
    async def test_post(request):
        return response.json({"POST": True})

    @app.route("/test_put", methods=['PUT'])
    async def test_put(request):
        return response.json({"PUT": True})

    @app.route("/test_delete", methods=['DELETE'])
    async def test_delete(request):
        return response.json({"DELETE": True})

    @app.route("/test_patch", methods=['PATCH'])
    async def test_patch(request):
        return response.json({"PATCH": True})

    @app.route("/test_options", methods=['OPTIONS'])
    async def test_options(request):
        return response.json({"OPTIONS": True})

    @app.route("/test_head", methods=['HEAD'])
    async def test_head(request):
        return response.json({"HEAD": True})

    @app.websocket("/test_ws")
    async def test_ws(request, ws):
        data = await ws.recv()
        await ws.send(data)

    return app

@pytest.fixture
def test_cli(loop, app, sanic_client):
    return loop.run_until_complete(sanic_client(app, protocol=WebSocketProtocol))

#########
# Tests #
#########

async def test_fixture_test_client_get(test_cli):
    """
    GET request
    """
    resp = await test_cli.get('/test_get')
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json == {"GET": True}

async def test_fixture_test_client_post(test_cli):
    """
    POST request
    """
    resp = await test_cli.post('/test_post')
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json == {"POST": True}

async def test_fixture_test_client_put(test_cli):
    """
    PUT request
    """
    resp = await test_cli.put('/test_put')
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json == {"PUT": True}

async def test_fixture_test_client_delete(test_cli):
    """
    DELETE request
    """
    resp = await test_cli.delete('/test_delete')
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json == {"DELETE": True}

async def test_fixture_test_client_patch(test_cli):
    """
    PATCH request
    """
    resp = await test_cli.patch('/test_patch')
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json == {"PATCH": True}

async def test_fixture_test_client_options(test_cli):
    """
    OPTIONS request
    """
    resp = await test_cli.options('/test_options')
    assert resp.status_code == 200
    
    resp_json = resp.json()
    assert resp_json == {"OPTIONS": True}

async def test_fixture_test_client_head(test_cli):
    """
    HEAD request
    """
    resp = await test_cli.head('/test_head')
    assert resp.status_code == 200
    print(type(resp))
    resp_body = resp.text
    # HEAD should not have body
    assert resp_body == ""

async def test_fixture_test_client_ws(test_cli):
    """
    Websockets
    """
    ws_conn = await test_cli.ws_connect('/test_ws')
    data = 'hello world!'
    await ws_conn.send(data)
    msg = await ws_conn.recv()
    assert msg == data
    await ws_conn.close()
