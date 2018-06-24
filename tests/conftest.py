import pytest
import requests
import websocket

import data.data_provider as provide
from client.client import HTTPClient, WSClient
from logic.test_case import HTTPTestCase, WSTestCase


@pytest.fixture(autouse=True)
def purge_all_links(request):
    requests.delete(
        url='http://localhost:8888/admin/all_links',
        json=dict(confirm='Yes')
    )


@pytest.fixture
def create_shortcut_link(request):
    create = requests.post(
        url='http://localhost:8888/shortcut',
        json=dict(link='https://github.com/Yurasb/url_shortener_testing')
    )
    return create


@pytest.fixture
def redirect_by_id(request, create_shortcut_link):
    requests.get(
        url='http://localhost:8888/r/{}'.format(
            create_shortcut_link.json()['id']
        )
    )


@pytest.fixture
def ws_connection(request):
    ws = websocket.create_connection('ws://127.0.0.1:8888/ws')

    def fin():
        ws.close()

    request.addfinalizer(fin)
    return ws


@pytest.fixture
def test_context(request, params):
    test_case = HTTPTestCase(params)
    return test_case


@pytest.fixture
def http_client(request):
    config = provide.client_configuration()
    return HTTPClient(config)


@pytest.fixture
def ws_client(request):
    config = provide.client_configuration()
    return WSClient(config)


@pytest.fixture(params=['TC1'])
def test_context(request):
    test_data = provide.test_data_by_id(request.param)
    return HTTPTestCase(test_data)


@pytest.fixture(params=['TC2'])
def ws_test_context(request):
    test_data = provide.test_data_by_id(request.param)
    return WSTestCase(test_data)


@pytest.fixture(params=['TC2'])
def expected_schema(request):
    schema = provide.expected_schema_by_id(request.param)
    return schema
