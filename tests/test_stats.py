import json
import uuid
import requests
import allure
from cerberus import Validator
from lxml import html


@allure.feature('Stats service')
@allure.story('Valid request status code')
def test_stats_status_code(
        purge_all_links, create_shortcut_link, redirect_by_id
):
    response = requests.post(
        url='http://localhost:8888/stats',
        data=json.dumps({'id': create_shortcut_link.json()['id']})
    )
    assert response.status_code == 200, (
        'Expected status code is 200, got {actual}'.format(
            actual=response.status_code
        )
    )


@allure.feature('Stats service')
@allure.story('Valid request not-redirected link response body')
def test_stats_new_body(purge_all_links, create_shortcut_link):
    response = requests.post(
        url='http://localhost:8888/stats',
        data=json.dumps({'id': create_shortcut_link.json()['id']})
    )

    v = Validator(
        {
            'last_redirected': {'nullable': True, 'type': 'float'},
            'redirects_count': {'type': 'integer', 'allowed': [0]}
        }
    )
    assert v.validate(response.json()), v.errors


@allure.feature('Stats service')
@allure.story('Valid request redirected link response body')
def test_stats_redirected_body(
        purge_all_links, create_shortcut_link, redirect_by_id
):
    response = requests.post(
        url='http://localhost:8888/stats',
        data=json.dumps({'id': create_shortcut_link.json()['id']})
    )

    v = Validator(
        {
            'last_redirected': {'nullable': False, 'type': 'float'},
            'redirects_count': {'type': 'integer', 'allowed': [1]}
        }
    )
    assert v.validate(response.json()), v.errors


@allure.feature('Stats service')
@allure.story('Invalid JSON data status code')
def test_stats_invalid_json_status_code(
        purge_all_links, create_shortcut_link
):
    response = requests.post(
        url='http://localhost:8888/stats',
        data=json.dumps(create_shortcut_link.json()['id'])
    )
    assert response.status_code == 500, (
        'Expected status code is 500, got {actual}'.format(
            actual=response.status_code
        )
    )


@allure.feature('Stats service')
@allure.story('Invalid JSON data response body')
def test_stats_invalid_json_body(
        purge_all_links, create_shortcut_link
):
    response = requests.post(
        url='http://localhost:8888/stats',
        data=json.dumps(create_shortcut_link.json()['id'])
    )

    parsed = html.fromstring(response.text)
    assert parsed.text_content()[:25] == '500 Internal Server Error', (
        'Expected title is "500 Internal Server Error", got {actual}'.format(
            actual=parsed.text_content()[:25]
        )
    )


@allure.feature('Stats service')
@allure.story('Invalid link ID status code')
def test_stats_invalid_id_status_code(purge_all_links):
    response = requests.post(
        url='http://localhost:8888/stats',
        data=json.dumps({'id': str(uuid.uuid4())})
    )
    assert response.status_code == 404, (
        'Expected status code is 404, got {actual}'.format(
            actual=response.status_code
        )
    )


@allure.feature('Stats service')
@allure.story('Invalid link ID response body')
def test_stats_invalid_id_body(purge_all_links):
    response = requests.post(
        url='http://localhost:8888/stats',
        data=json.dumps({'id': str(uuid.uuid4())})
    )

    v = Validator(
        {
            'status': {'type': 'integer', 'allowed': [404]},
            'message': {'type': 'string', 'allowed': ['Not Found']}
        }
    )
    assert v.validate(response.json()), v.errors


@allure.feature('Stats service')
@allure.story('Invalid method status code')
def test_stats_wrong_method_status_code():
    response = requests.get(
        url='http://localhost:8888/stats',
    )
    assert response.status_code == 405, (
        'Expected status code is 405, got {actual}'.format(
            actual=response.status_code
        )
    )


@allure.feature('Stats service')
@allure.story('Invalid method response body')
def test_stats_wrong_method_body():
    response = requests.get(
        url='http://localhost:8888/stats',
    )

    v = Validator(
        {
            'status': {'type': 'integer', 'allowed': [405]},
            'message': {
                'type': 'string', 'allowed': ['Method Not Allowed']
            }
        }
    )
    assert v.validate(response.json()), v.errors
