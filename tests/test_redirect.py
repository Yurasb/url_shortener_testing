import uuid

from cerberus import Validator
from requests import request


def test_redirect_status_code():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    create = request(
        method='POST',
        url='http://localhost:8888/shortcut',
        data='{ "link": "https://github.com/Yurasb/url_shortener_testing"}'
    )
    # action
    response = request(
        method='GET',
        url='http://localhost:8888/r/{}'.format(create.json()['id'])
    )
    # validation
    assert response.status_code == 302


def test_redirect_is_redirect():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    create = request(
        method='POST',
        url='http://localhost:8888/shortcut',
        data='{ "link": "https://github.com/Yurasb/url_shortener_testing"}'
    )
    # action
    response = request(
        method='GET',
        url='http://localhost:8888/r/{}'.format(create.json()['id'])
    )
    # validation
    assert response.is_redirect


def test_redirect_body():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    create = request(
        method='POST',
        url='http://localhost:8888/shortcut',
        data='{ "link": "https://github.com/Yurasb/url_shortener_testing"}'
    )
    # action
    response = request(
        method='GET',
        url='http://localhost:8888/r/{}'.format(create.json()['id'])
    )
    # validation - to be completed using XML-schema
    assert response.content


def test_redirect_wrong_method_status_code():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    create = request(
        method='POST',
        url='http://localhost:8888/shortcut',
        data='{ "link": "https://github.com/Yurasb/url_shortener_testing"}'
    )
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/r/{}'.format(create.json()['id']),
        data='{}'
    )
    # validation
    assert response.status_code == 405


def test_redirect_wrong_method_body():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    create = request(
        method='POST',
        url='http://localhost:8888/shortcut',
        data='{ "link": "https://github.com/Yurasb/url_shortener_testing"}'
    )
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/r/{}'.format(create.json()['id']),
        data='{}'
    )
    # validation
    v = Validator(
        {
            'status': {'type': 'integer', 'allowed': [405]},
            'message': {'type': 'string', 'allowed': ['Method Not Allowed']}
        }
    )
    assert v.validate(response.json())


def test_redirect_invalid_id_status_code():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # action
    response = request(
        method='GET',
        url='http://localhost:8888/r/{}'.format(uuid.uuid4())
    )
    # validation
    assert response.status_code == 404


def test_redirect_invalid_id_body():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # action
    response = request(
        method='GET',
        url='http://localhost:8888/r/{}'.format(uuid.uuid4())
    )
    # validation
    v = Validator(
        {
            'status': {'type': 'integer', 'allowed': [404]},
            'message': {'type': 'string', 'allowed': ['Not Found']}
        }
    )
    assert v.validate(response.json())
