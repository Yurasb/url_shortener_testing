import allure
import requests
from cerberus import Validator
from lxml import html


@allure.feature('Delete handler')
@allure.story('Valid request status code')
def test_delete_all_links_status_code(create_shortcut_link):
    response = requests.delete(
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
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
        data='{"Are you sure?":"Yes"}'
    )

    check = requests.get(
        url='http://localhost:8888/admin/all_links'
    )
    v = Validator({'links': {}})
    assert v.validate(check.json()), v.errors


@allure.feature('Delete handler')
@allure.story('Invalid method status code')
def test_delete_all_links_wrong_method_status_code():
    response = requests.post(
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
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
        data='{"Are you sure?":"Yes"}'
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


@allure.feature('Delete handler')
@allure.story('No confirmation status code')
def test_delete_all_links_no_confirmation_status_code():
    response = requests.delete(
        url='http://localhost:8888/admin/all_links'
    )
    assert response.status_code == 500, (
        'Expected status code is 500, got {actual}'.format(
            actual=response.status_code
        )
    )


@allure.feature('Delete handler')
@allure.story('No confirmation response body')
def test_delete_all_links_no_confirmation_body():
    response = requests.delete(
        url='http://localhost:8888/admin/all_links'
    )

    parsed = html.fromstring(response.text)
    assert parsed.text_content()[:25] == '500 Internal Server Error', (
        'Expected title is "500 Internal Server Error", got {actual}'.format(
            actual=parsed.text_content()[:25]
        )
    )
