import pytest
import requests
import websocket


@pytest.fixture
def purge_all_links(request):
    requests.delete(
        url='http://localhost:8888/admin/all_links',
        data='{"confirm":"Yes"}'
    )


@pytest.fixture
def create_shortcut_link(request):
    create = requests.post(
        url='http://localhost:8888/shortcut',
        data='{ "link": "https://github.com/Yurasb/url_shortener_testing"}'
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
