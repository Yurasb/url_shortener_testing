import json
import uuid

from cerberus import Validator
from requests import request


def test_stats_status_code():
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
    request(
        method='GET',
        url='http://localhost:8888/r/{}'.format(create.json()['id'])
    )
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/stats',
        data=json.dumps({'id': create.json()['id']})
    )
    # validation
    assert response.status_code == 200


def test_stats_new_body():
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
        url='http://localhost:8888/stats',
        data=json.dumps({'id': create.json()['id']})
    )
    # validation
    v = Validator(
        {
            'last_redirected': {'nullable': True, 'type': 'float'},
            'redirects_count': {'type': 'integer', 'allowed': [0]}
        }
    )
    assert v.validate(response.json())


def test_stats_redirected_body():
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
    request(
        method='GET',
        url='http://localhost:8888/r/{}'.format(create.json()['id'])
    )
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/stats',
        data=json.dumps({'id': create.json()['id']})
    )
    # validation
    v = Validator(
        {
            'last_redirected': {'nullable': False, 'type': 'float'},
            'redirects_count': {'type': 'integer', 'allowed': [1]}
        }
    )
    assert v.validate(response.json())


def test_stats_invalid_json_status_code():
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
        url='http://localhost:8888/stats',
        data=json.dumps(create.json()['id'])
    )
    # validation
    assert response.status_code == 500


def test_stats_invalid_json_body():
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
        url='http://localhost:8888/stats',
        data=json.dumps(create.json()['id'])
    )
    # validation - to be completed with XML-schema
    assert response.content


def test_stats_invalid_id_status_code():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/stats',
        data=json.dumps({'id': str(uuid.uuid4())})
    )
    # validation
    assert response.status_code == 404


def test_stats_invalid_id_body():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/stats',
        data=json.dumps({'id': str(uuid.uuid4())})
    )
    # validation
    v = Validator(
        {
            'status': {'type': 'integer', 'allowed': [404]},
            'message': {'type': 'string', 'allowed': ['Not Found']}
        }
    )
    assert v.validate(response.json())


def test_stats_wrong_method_status_code():
    # action
    response = request(
        method='GET',
        url='http://localhost:8888/stats',
    )
    # validation
    assert response.status_code == 405


def test_stats_wrong_method_body():
    # action
    response = request(
        method='GET',
        url='http://localhost:8888/stats',
    )
    # validation
    v = Validator(
        {
            'status': {'type': 'integer', 'allowed': [405]},
            'message': {'type': 'string', 'allowed': ['Method Not Allowed']}
        }
    )
    assert v.validate(response.json())
