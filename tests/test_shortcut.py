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

    assert response.status_code == 200


def test_shortcut_body(purge_all_links):
    response = requests.post(
        url='http://localhost:8888/shortcut',
        data=json.dumps({'link': URL})
    )

    v = Validator(
        {
            'id': {
                'type': 'string', 'allowed': [response.json()['id']]
            }
        }
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
    assert URL in json.dumps(check.json())


def test_shortcut_wrong_method_status_code():
    response = requests.get(
        url='http://localhost:8888/shortcut'
    )
    assert response.status_code == 405


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

    assert response.status_code == 500


def test_shortcut_invalid_json_body():
    response = requests.post(
        url='http://localhost:8888/shortcut',
        data='{ "link" "https://github.com/Yurasb/url_shortener_testing"}'
    )

    parsed = html.fromstring(response.text)
    assert parsed.text_content()[:25] == '500 Internal Server Error'


def test_shortcut_invalid_link():
    response = requests.post(
        url='http://localhost:8888/shortcut',
        data='{"link": "github.com/Yurasb/url_shortener_testing"}'
    )
    assert response.status_code == 400
