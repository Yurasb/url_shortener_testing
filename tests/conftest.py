import pytest
import requests


@pytest.fixture
def purge_all_links(request):
    requests.delete(
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
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
