import json
import requests
from cerberus import Validator
from lxml import html


URL = 'https://github.com/Yurasb/url_shortener_testing'


def test_shortcut_status_code(purge_all_links):
    response = requests.post(
        url='http://localhost:8888/shortcut',
        data=json.dumps({'link': URL})
    )
    assert response.status_code == 200, (
        'Expected status code is 200, got {actual}'.format(
            actual=response.status_code
        )
    )


def test_shortcut_body(purge_all_links):
    response = requests.post(
        url='http://localhost:8888/shortcut',
        data=json.dumps({'link': URL})
    )

    v = Validator(
        {'id': {'type': 'string', 'allowed': [response.json()['id']]}}
    )
    assert v.validate(response.json()), v.errors


def test_shortcut_created(purge_all_links):
    requests.post(
        url='http://localhost:8888/shortcut',
        data=json.dumps({'link': URL})
    )

    check = requests.get(
        url='http://localhost:8888/admin/all_links'
    )
    assert URL in json.dumps(check.json()), (
        '{url} is not found in shortcut list'.format(url=URL)
    )


def test_shortcut_wrong_method_status_code():
    response = requests.get(
        url='http://localhost:8888/shortcut'
    )
    assert response.status_code == 405, (
        'Expected status code is 405, got {actual}'.format(
            actual=response.status_code
        )
    )


def test_shortcut_wrong_method_body():
    response = requests.get(
        url='http://localhost:8888/shortcut'
    )

    v = Validator(
        {
            'status': {'type': 'integer', 'allowed': [405]},
            'message': {'type': 'string', 'allowed': ['Method Not Allowed']}
        }
    )
    assert v.validate(response.json()), v.errors


def test_shortcut_invalid_json_status_code():
    response = requests.post(
        url='http://localhost:8888/shortcut',
        data='{ "link" "https://github.com/Yurasb/url_shortener_testing"}'
    )
    assert response.status_code == 500, (
        'Expected status code is 500, got {actual}'.format(
            actual=response.status_code
        )
    )


def test_shortcut_invalid_json_body():
    response = requests.post(
        url='http://localhost:8888/shortcut',
        data='{ "link" "https://github.com/Yurasb/url_shortener_testing"}'
    )

    parsed = html.fromstring(response.text)
    assert parsed.text_content()[:25] == '500 Internal Server Error', (
        'Expected title is "500 Internal Server Error", got {actual}'.format(
            actual=parsed.text_content()[:25]
        )
    )


def test_shortcut_invalid_link():
    response = requests.post(
        url='http://localhost:8888/shortcut',
        data='{"link": "github.com/Yurasb/url_shortener_testing"}'
    )
    assert response.status_code == 400, (
        'Expected status code is 400, got {actual}'.format(
            actual=response.status_code
        )
    )
