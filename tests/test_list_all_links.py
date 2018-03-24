import json
import allure
import requests
from cerberus import Validator


@allure.feature('List all links handler')
@allure.story('Valid request with empty list status code')
def test_list_all_links_empty_status_code():
    response = requests.get(
        url='http://localhost:8888/admin/all_links'
    )
    assert response.status_code == 200, (
        'Expected status code 200, got {actual}'.format(
            actual=response.status_code
        )
    )


@allure.feature('List all links handler')
@allure.story('Valid request with empty list response body')
def test_list_all_links_empty_body():
    response = requests.get(
        url='http://localhost:8888/admin/all_links'
    )

    v = Validator(dict(links=dict()))
    assert v.validate(response.json()), v.errors


@allure.feature('List all links handler')
@allure.story('Valid request with not empty list status code')
def test_list_all_links_not_empty_status_code(create_shortcut_link):
    response = requests.get(
        url='http://localhost:8888/admin/all_links'
    )
    assert response.status_code == 200, (
        'Expected status code is 200, got {actual}'.format(
            actual=response.status_code
        )
    )


@allure.feature('List all links handler')
@allure.story('Valid WebSocket request with empty link list')
def test_ws_list_all_links_empty(ws_connection):
    ws_connection.send(json.dumps(
        dict(command='get_all_links', body=dict())
    ))
    response = ws_connection.recv()

    v = Validator(
        dict(code=dict(type='integer', allowed=[200]),
             body=dict(type='dict', schema=dict(links=dict(empty=True))))
    )
    assert v.validate(json.loads(response)), v.errors


@allure.feature('List all links handler')
@allure.story('Valid request with not empty list response body')
def test_list_all_links_not_empty_body(create_shortcut_link):
    response = requests.get(
        url='http://localhost:8888/admin/all_links'
    )

    v = Validator(
        dict(links=dict(type='dict', schema={
            str(create_shortcut_link.json()['id']): dict(
                type='string', allowed=['https://github.com/Yurasb/url_shortener_testing']
            )
        }))
    )
    assert v.validate(response.json()), v.errors


@allure.feature('List all links handler')
@allure.story('Valid WebSocket request with not empty link list')
def test_ws_list_all_links_not_empty(create_shortcut_link, ws_connection):
    ws_connection.send(json.dumps(
        dict(command='get_all_links', body=dict())
    ))
    response = ws_connection.recv()

    v = Validator(
        dict(code=dict(type='integer', allowed=[200]),
             body=dict(type='dict', schema=dict(
                 links=dict(type='dict', schema={
                     str(create_shortcut_link.json()['id']): dict(
                         type='string', allowed=['https://github.com/Yurasb/url_shortener_testing']
                     )}))))
    )
    assert v.validate(json.loads(response)), v.errors


@allure.feature('List all links handler')
@allure.story('Invalid method status code')
def test_list_all_links_wrong_method_status_code():
    response = requests.post(
        url='http://localhost:8888/admin/all_links',
        json=dict()
    )
    assert response.status_code == 405, (
        'Expected status code is 405, got {actual}'.format(
            actual=response.status_code
        )
    )


@allure.feature('List all links handler')
@allure.story('Invalid method response body')
def test_all_links_wrong_method_body():
    response = requests.post(
        url='http://localhost:8888/admin/all_links',
        json=dict()
    )

    v = Validator(
        dict(status=dict(type='integer', allowed=[405]),
             message=dict(type='string', allowed=['Method Not Allowed']))
    )
    assert v.validate(response.json()), v.errors


@allure.feature('List all links handler')
@allure.story('WebSoc')
def test_ws_list_all_links_no_body(ws_connection):
    ws_connection.send(json.dumps(
        dict(command='get_all_links')
    ))
    response = ws_connection.recv()

    v = Validator(
        dict(code=dict(type='integer', allowed=[400]),
             error=dict(type='dict', schema=dict(
                 body=dict(type='list', allowed=['required field'])
             )))
    )
    assert v.validate(json.loads(response)), v.errors
