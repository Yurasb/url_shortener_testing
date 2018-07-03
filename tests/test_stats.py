import json
import uuid
import allure
import requests
from cerberus import Validator
from lxml import html


@allure.feature('Stats handler')
@allure.story('Valid request status code')
def test_stats_status_code(create_shortcut_link, redirect_by_id):
    response = requests.post(
        url='http://localhost:8888/stats',
        json=dict(id=create_shortcut_link.json()['id'])
    )
    assert response.status_code == 200, (
        'Expected status code is 200, got {actual}'.format(
            actual=response.status_code
        )
    )


@allure.feature('Stats handler')
@allure.story('Valid request not-redirected link response body')
def test_stats_new_body(create_shortcut_link):
    response = requests.post(
        url='http://localhost:8888/stats',
        json=dict(id=create_shortcut_link.json()['id'])
    )

    v = Validator(
        dict(last_redirected=dict(nullable=True, type='float'),
             redirects_count=dict(type='integer', allowed=[0]))
    )
    assert v.validate(response.json()), v.errors


@allure.feature('Stats handler')
@allure.story('Valid request redirected link response body')
def test_stats_redirected_body(create_shortcut_link, redirect_by_id):
    response = requests.post(
        url='http://localhost:8888/stats',
        json=dict(id=create_shortcut_link.json()['id'])
    )

    v = Validator(
        dict(last_redirected=dict(nullable=False, type='float'),
             redirects_count=dict(type='integer', allowed=[1]))
    )
    assert v.validate(response.json()), v.errors


@allure.feature('Stats handler')
@allure.story('Valid WebSocket query not-redirected link')
def test_ws_stats_valid_query_new(create_shortcut_link, ws_connection):
    ws_connection.send(json.dumps(
        dict(command='get_stats',
             body=dict(id=create_shortcut_link.json()['id'])
             )))
    response = ws_connection.recv()

    v = Validator(
        dict(code=dict(type='integer', allowed=[200]),
             body=dict(type='dict', schema=dict(
                 last_redirected=dict(nullable=True, type='float'),
                 redirects_count=dict(type='integer', allowed=[0])
             )))
    )
    assert v.validate(json.loads(response)), v.errors


@allure.feature('Stats handler')
@allure.story('Valid WebSocket query redirected link')
def test_ws_stats_valid_query_redirected(
        create_shortcut_link, redirect_by_id, ws_connection
):
    ws_connection.send(json.dumps(
        dict(command='get_stats', body=dict(id=create_shortcut_link.json()['id']))
    ))
    response = ws_connection.recv()

    v = Validator(
        dict(code=dict(type='integer', allowed=[200]),
             body=dict(type='dict', schema=dict(
                 last_redirected=dict(nullable=False, type='float'),
                 redirects_count=dict(type='integer', allowed=[1])
             )))
    )
    assert v.validate(json.loads(response)), v.errors


@allure.feature('Stats handler')
@allure.story('Invalid JSON data status code')
def test_stats_invalid_json_status_code(create_shortcut_link):
    response = requests.post(
        url='http://localhost:8888/stats',
        data=json.dumps(create_shortcut_link.json()['id'])
    )
    assert response.status_code == 500, (
        'Expected status code is 500, got {actual}'.format(
            actual=response.status_code
        )
    )


@allure.feature('Stats handler')
@allure.story('Invalid JSON data response body')
def test_stats_invalid_json_body(create_shortcut_link):
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


@allure.feature('Stats handler')
@allure.story('Invalid link ID status code')
def test_stats_invalid_id_status_code():
    response = requests.post(
        url='http://localhost:8888/stats',
        json=dict(id=str(uuid.uuid4()))
    )
    assert response.status_code == 404, (
        'Expected status code is 404, got {actual}'.format(
            actual=response.status_code
        )
    )


@allure.feature('Stats handler')
@allure.story('Invalid link ID response body')
def test_stats_invalid_id_body():
    response = requests.post(
        url='http://localhost:8888/stats',
        json=dict(id=str(uuid.uuid4()))
    )

    v = Validator(
        dict(status=dict(type='integer', allowed=[404]),
             message=dict(type='string', allowed=['Not Found']))
    )
    assert v.validate(response.json()), v.errors


@allure.feature('Stats handler')
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


@allure.feature('Stats handler')
@allure.story('Invalid method response body')
def test_stats_wrong_method_body():
    response = requests.get(
        url='http://localhost:8888/stats',
    )

    v = Validator(
        dict(status=dict(type='integer', allowed=[405]),
             message=dict(type='string', allowed=['Method Not Allowed']))
    )
    assert v.validate(response.json()), v.errors


@allure.feature('Stats handler')
@allure.story('WebSocket query with invalid link ID')
def test_ws_stats_invalid_id(ws_connection):
    ws_connection.send(json.dumps(
        dict(command='get_stats', body=dict(id=str(uuid.uuid4())[10]))
    ))
    response = ws_connection.recv()

    v = Validator(
        dict(code=dict(type='integer', allowed=[404]),
             error=dict(type='string', allowed=['Not Found']))
    )
    assert v.validate(json.loads(response)), v.errors
