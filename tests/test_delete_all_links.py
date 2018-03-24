import json
import allure
import requests
from cerberus import Validator


@allure.feature('Delete handler')
@allure.story('Valid request status code')
def test_delete_all_links_status_code(create_shortcut_link):
    response = requests.delete(
        url='http://localhost:8888/admin/all_links',
        json=dict(confirm='Yes')
    )
    assert response.status_code == 200, (
        'Expected status code is 200, got {actual}'.format(
            actual=response.status_code
        )
    )


@allure.feature('Delete handler')
@allure.story('Check if all links removed')
def test_delete_all_links_removed(create_shortcut_link):
    requests.delete(
        url='http://localhost:8888/admin/all_links',
        json=dict(confirm='Yes')
    )

    check = requests.get(
        url='http://localhost:8888/admin/all_links'
    )
    v = Validator(dict(links={}))
    assert v.validate(check.json()), v.errors


@allure.feature('Delete handler')
@allure.story('Valid WebSocket query')
def test_ws_delete_all_links_valid_query(
        create_shortcut_link, ws_connection
):
    ws_connection.send(json.dumps(
        dict(command='purge_all', body=dict(confirm='yes'))
    ))
    response = ws_connection.recv()

    v = Validator(
        dict(code=dict(type='integer', allowed=[200]), body=dict(empty=True))
    )
    assert v.validate(json.loads(response)), v.errors


@allure.feature('Delete handler')
@allure.story('Invalid method status code')
def test_delete_all_links_wrong_method_status_code():
    response = requests.post(
        url='http://localhost:8888/admin/all_links',
        json={'Are you sure?': 'Yes'}
    )
    assert response.status_code == 405, (
        'Expected status code is 405, got {actual}'.format(
            actual=response.status_code
        )
    )


@allure.feature('Delete handler')
@allure.story('Invalid method response body')
def test_delete_all_links_wrong_method_body():
    response = requests.post(
        url='http://localhost:8888/admin/all_links',
        json=dict(confirm='Yes')
    )

    v = Validator(
        dict(status=dict(type='integer', allowed=[405]),
             message=dict(type='string', allowed=['Method Not Allowed']))
    )
    assert v.validate(response.json()), v.errors


@allure.feature('Delete handler')
@allure.story('No confirmation status code')
def test_delete_all_links_no_confirmation_status_code():
    response = requests.delete(
        url='http://localhost:8888/admin/all_links'
    )
    assert response.status_code == 406, (
        'Expected status code is 406, got {actual}'.format(
            actual=response.status_code
        )
    )


@allure.feature('Delete handler')
@allure.story('No confirmation response body')
def test_delete_all_links_no_confirmation_body():
    response = requests.delete(
        url='http://localhost:8888/admin/all_links'
    )

    v = Validator(
        dict(message=dict(type='string', allowed=['Invalid json']),
             status=dict(type='integer', allowed=[406]))
    )
    assert v.validate(response.json()), v.errors


@allure.feature('Delete handler')
@allure.story('Valid WebSocket query with no confirmation')
def test_ws_delete_all_links_no_confirmation(ws_connection):
    ws_connection.send(json.dumps(
        dict(command='purge_all', body=dict(confirm='no'))
    ))
    response = ws_connection.recv()

    v = Validator(
        dict(code=dict(type='integer', allowed=[400]),
             error=dict(type='dict', schema=dict(
                 confirm=dict(type='list', allowed=['unallowed value no'])
             )))
    )
    assert v.validate(json.loads(response)), v.errors


@allure.feature('Delete handler')
@allure.story('WebSocket query without confirmation field')
def test_ws_delete_all_links_confirm_missing(ws_connection):
    ws_connection.send(json.dumps(
        dict(command='purge_all', body=dict())
    ))
    response = ws_connection.recv()

    v = Validator(
        dict(code=dict(type='integer', allowed=[400]),
             error=dict(type='dict', schema=dict(
                 confirm=dict(type='list', allowed=['required field'])
             )))
    )
    assert v.validate(json.loads(response)), v.errors
