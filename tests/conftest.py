import pytest
import requests

from data.data_helpers import get_data_by_id, get_schema_by_id


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


@pytest.fixture(params=['TC1'])
def payload(request):
    test_data = get_data_by_id(request.param)
    return test_data


@pytest.fixture(params=['TC2'])
def expected_schema(request):
    schema = get_schema_by_id(request.param)
    return schema
