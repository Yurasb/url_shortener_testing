import pytest

from data.context import LinkContext
from steps.http_steps import create_link, get_all_links
from tests import is_json_content_valid


@pytest.fixture(scope='function')
def data(request):
    context = LinkContext(
        link='https://github.com/Yurasb/url_shortener_testing'
    )
    return context


def test_status_code(data):
    response = create_link(data.link)
    assert response.status_code == 200


def test_body(data):
    response = create_link(data.link)
    assert is_json_content_valid(
        {'id': {'type': 'string'}}, response.json()
    )


def test_link_created(data):
    response = get_all_links()
    assert data.link in response.json()['links']
