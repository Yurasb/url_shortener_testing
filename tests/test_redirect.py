import uuid
import requests
from cerberus import Validator


def test_redirect_status_code(purge_all_links, create_shortcut_link):
    response = requests.get(
        url='http://localhost:8888/r/{}'.format(
            create_shortcut_link.json()['id']
        ),
        allow_redirects=False)
    assert response.status_code == 302


def test_redirect_is_redirect(purge_all_links, create_shortcut_link):
    response = requests.get(
        url='http://localhost:8888/r/{}'.format(
            create_shortcut_link.json()['id']
        ),
        allow_redirects=False
    )
    assert response.is_redirect


def test_redirect_location(purge_all_links, create_shortcut_link):
    response = requests.get(
        url='http://localhost:8888/r/{}'.format(
            create_shortcut_link.json()['id']
        ),
        allow_redirects=False
    )
    assert response.headers['Location'] == 'https://github.com/Yurasb/url_shortener_testing'


def test_redirect_body(purge_all_links, create_shortcut_link):
    response = requests.get(
        url='http://localhost:8888/r/{}'.format(
            create_shortcut_link.json()['id']
        ),
        allow_redirects=False
    )
    assert response.text == '302: Found'


def test_redirect_wrong_method_status_code(purge_all_links, create_shortcut_link):
    response = requests.post(
        url='http://localhost:8888/r/{}'.format(
            create_shortcut_link.json()['id']
        ),
        data='{}'
    )
    assert response.status_code == 405


def test_redirect_wrong_method_body(purge_all_links, create_shortcut_link):
    response = requests.post(
        url='http://localhost:8888/r/{}'.format(
            create_shortcut_link.json()['id']
        ),
        data='{}'
    )

    v = Validator(
        {
            'status': {'type': 'integer', 'allowed': [405]},
            'message': {'type': 'string', 'allowed': ['Method Not Allowed']}
        }
    )
    assert v.validate(response.json()), v.errors


def test_redirect_invalid_id_status_code(purge_all_links):
    response = requests.get(
        url='http://localhost:8888/r/{}'.format(uuid.uuid4())
    )
    assert response.status_code == 404


def test_redirect_invalid_id_body(purge_all_links):
    response = requests.get(
        url='http://localhost:8888/r/{}'.format(uuid.uuid4())
    )

    v = Validator(
        {
            'status': {'type': 'integer', 'allowed': [404]},
            'message': {'type': 'string', 'allowed': ['Not Found']}
        }
    )
    assert v.validate(response.json()), v.errors
