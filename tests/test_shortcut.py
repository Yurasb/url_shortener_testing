import json

from cerberus import Validator
from requests import request


def test_shortcut_status_code():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/shortcut',
        data='{ "link": "https://github.com/Yurasb/url_shortener_testing"}'
    )
    # validation
    assert response.status_code == 200


def test_shortcut_body():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/shortcut',
        data='{ "link": "https://github.com/Yurasb/url_shortener_testing"}'
    )
    # validation
    v = Validator(
        {
            'id': {
                'type': 'string', 'allowed': [response.json()['id']]
            }
        }
    )
    assert v.validate(response.json())


def test_shortcut_created():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # action
    request(
        method='POST',
        url='http://localhost:8888/shortcut',
        data='{ "link": "https://github.com/Yurasb/url_shortener_testing"}'
    )
    # validation
    check = request(
        method='GET',
        url='http://localhost:8888/admin/all_links'
    )
    assert "https://github.com/Yurasb/url_shortener_testing" in json.dumps(check.json())


def test_shortcut_wrong_method_status_code():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # action
    response = request(
        method='GET',
        url='http://localhost:8888/shortcut'
    )
    # validation
    assert response.status_code == 405


def test_shortcut_wrong_method_body():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # action
    response = request(
        method='GET',
        url='http://localhost:8888/shortcut'
    )
    # validation
    v = Validator(
        {
            'status': {'type': 'integer', 'allowed': [405]},
            'message': {'type': 'string', 'allowed': ['Method Not Allowed']}
        }
    )
    assert v.validate(response.json())


def test_shortcut_invalid_json_status_code():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/shortcut',
        data='{ "link" "https://github.com/Yurasb/url_shortener_testing"}'
    )
    # validation
    assert response.status_code == 500


def test_shortcut_invalid_json_body():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/shortcut',
        data='{ "link" "https://github.com/Yurasb/url_shortener_testing"}'
    )
    # validation - to be completed with XML-schema
    assert response.content


def test_shortcut_invalid_link():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/shortcut',
        data='{ "link": "github.com/Yurasb/url_shortener_testing"}'
    )
    # validation
    assert response.status_code == 400
