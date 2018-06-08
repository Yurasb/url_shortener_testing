import pytest
import requests
import websocket

from client.client import HTTPClient
from data.data_provider import DataProvider
from logic.test_case import TestCase


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
    test_case = TestCase(params)
    return test_case


@pytest.fixture
def http_client(request):
    config = DataProvider.provide_config_for('http')
    return HTTPClient(config)


@pytest.fixture(params=['TC1'])
def test_context(request):
    test_data = DataProvider.provide_test_data_by_id(request.param)
    return TestCase(test_data)


@pytest.fixture(params=['TC1'])
def expected_schema(request):
    schema = DataProvider.provide_expected_schema_by_id(request.param)
    return schema
