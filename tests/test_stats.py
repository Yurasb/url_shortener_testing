import json
import uuid
import requests

from cerberus import Validator


def test_stats_status_code(
        purge_all_links, create_shortcut_link, redirect_by_id
):
    # precondition
    purge_all_links
    create_shortcut_link
    redirect_by_id
    # action
    response = requests.post(
        url='http://localhost:8888/stats',
        data=json.dumps({'id': create_shortcut_link.json()['id']})
    )
    # validation
    assert response.status_code == 200


def test_stats_new_body(purge_all_links, create_shortcut_link):
    # precondition
    purge_all_links
    create_shortcut_link
    # action
    response = requests.post(
        url='http://localhost:8888/stats',
        data=json.dumps({'id': create_shortcut_link.json()['id']})
    )
    # validation
    v = Validator(
        {
            'last_redirected': {'nullable': True, 'type': 'float'},
            'redirects_count': {'type': 'integer', 'allowed': [0]}
        }
    )
    assert v.validate(response.json()), v.errors


def test_stats_redirected_body(
        purge_all_links, create_shortcut_link, redirect_by_id
):
    # precondition
    purge_all_links
    create_shortcut_link
    redirect_by_id
    # action
    response = requests.post(
        url='http://localhost:8888/stats',
        data=json.dumps({'id': create_shortcut_link.json()['id']})
    )
    # validation
    v = Validator(
        {
            'last_redirected': {'nullable': False, 'type': 'float'},
            'redirects_count': {'type': 'integer', 'allowed': [1]}
        }
    )
    assert v.validate(response.json()), v.errors


def test_stats_invalid_json_status_code(
        purge_all_links, create_shortcut_link
):
    # precondition
    purge_all_links
    create_shortcut_link
    # action
    response = requests.post(
        url='http://localhost:8888/stats',
        data=json.dumps(create_shortcut_link.json()['id'])
    )
    # validation
    assert response.status_code == 500


def test_stats_invalid_json_body(
        purge_all_links, create_shortcut_link
):
    # precondition
    purge_all_links
    create_shortcut_link
    # action
    response = requests.post(
        url='http://localhost:8888/stats',
        data=json.dumps(create_shortcut_link.json()['id'])
    )
    # validation - to be completed with XML-schema
    assert response.content


def test_stats_invalid_id_status_code(purge_all_links):
    # precondition
    purge_all_links
    # action
    response = requests.post(
        url='http://localhost:8888/stats',
        data=json.dumps({'id': str(uuid.uuid4())})
    )
    # validation
    assert response.status_code == 404


def test_stats_invalid_id_body(purge_all_links):
    # precondition
    purge_all_links
    # action
    response = requests.post(
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
    assert v.validate(response.json()), v.errors


def test_stats_wrong_method_status_code():
    # action
    response = requests.get(
        url='http://localhost:8888/stats',
    )
    # validation
    assert response.status_code == 405


def test_stats_wrong_method_body():
    # action
    response = requests.get(
        url='http://localhost:8888/stats',
    )
    # validation
    v = Validator(
        {
            'status': {'type': 'integer', 'allowed': [405]},
            'message': {
                'type': 'string', 'allowed': ['Method Not Allowed']
            }
        }
    )
    assert v.validate(response.json()), v.errors
