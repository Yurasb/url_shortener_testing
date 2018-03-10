import allure
import requests
from cerberus import Validator


@allure.feature('List all links service')
@allure.story('Valid request with empty list status code')
def test_list_all_links_empty_status_code(purge_all_links):
    response = requests.get(
        url='http://localhost:8888/admin/all_links'
    )
    assert response.status_code == 200, (
        'Expected status code 200, got {actual}'.format(
            actual=response.status_code
        )
    )


@allure.feature('List all links service')
@allure.story('Valid request with empty list response body')
def test_list_all_links_empty_body(purge_all_links):
    response = requests.get(
        url='http://localhost:8888/admin/all_links'
    )

    v = Validator({'links': {}})
    assert v.validate(response.json()), v.errors


@allure.feature('List all links service')
@allure.story('Valid request with not empty list status code')
def test_list_all_links_not_empty_status_code(
        purge_all_links, create_shortcut_link
):
    response = requests.get(
        url='http://localhost:8888/admin/all_links'
    )
    assert response.status_code == 200, (
        'Expected status code is 200, got {actual}'.format(
            actual=response.status_code
        )
    )


@allure.feature('List all links service')
@allure.story('Valid request with not empty list response body')
def test_list_all_links_not_empty_body(
        purge_all_links, create_shortcut_link
):
    response = requests.get(
        url='http://localhost:8888/admin/all_links'
    )

    v = Validator(
        {
            'links': {
                'type': 'dict', 'schema': {
                    str(create_shortcut_link.json()['id']): {
                        'type': 'string',
                        'allowed': ['https://github.com/Yurasb/url_shortener_testing']
                    }
                }
            }
        }
    )
    assert v.validate(response.json()), v.errors


@allure.feature('List all links service')
@allure.story('Invalid method status code')
def test_list_all_links_wrong_method_status_code():
    response = requests.post(
        url='http://localhost:8888/admin/all_links',
        data='{}'
    )
    assert response.status_code == 405, (
        'Expected status code is 405, got {actual}'.format(
            actual=response.status_code
        )
    )


@allure.feature('List all links service')
@allure.story('Invalid method response body')
def test_all_links_wrong_method_body():
    response = requests.post(
        url='http://localhost:8888/admin/all_links',
        data='{}'
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
