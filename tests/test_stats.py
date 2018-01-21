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
            'redirects_count': {'type': 'integer', 'min': 0, 'max': 0}
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
            'redirects_count': {'type': 'integer', 'min': 1, 'max': 1}
        }
    )
    assert v.validate(response.json())


def test_stats_invalid_json():
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
        data=json.dumps({create.json()['id']})
    )
    # validation
    assert response.status_code == 400


def test_stats_invalid_id():
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
        data=json.dumps({'id': uuid.uuid4()})
    )
    # validation
    assert response.status_code == 404


def test_stats_wrong_method():
    # action
    response = request(
        method='GET',
        url='http://localhost:8888/stats',
    )
    # validation
    assert response.status_code == 406
