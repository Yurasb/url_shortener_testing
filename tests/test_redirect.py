import uuid
import allure
import requests
from cerberus import Validator


URL = 'https://github.com/Yurasb/url_shortener_testing'


@allure.feature('Redirect service')
@allure.story('Valid request status code')
def test_redirect_status_code(
        purge_all_links, create_shortcut_link
):
    response = requests.get(
        url='http://localhost:8888/r/{}'.format(
            create_shortcut_link.json()['id']
        ),
        allow_redirects=False
    )
    assert response.status_code == 302, (
        'Expected status code is 302, got {actual}'.format(
            actual=response.status_code
        )
    )


@allure.feature('Redirect service')
@allure.story('Valid request is redirected')
def test_redirect_is_redirect(
        purge_all_links, create_shortcut_link
):
    response = requests.get(
        url='http://localhost:8888/r/{}'.format(
            create_shortcut_link.json()['id']
        ),
        allow_redirects=False
    )
    assert response.is_redirect


@allure.feature('Redirect service')
@allure.story('Valid request redirect location')
def test_redirect_location(
        purge_all_links, create_shortcut_link
):
    response = requests.get(
        url='http://localhost:8888/r/{}'.format(
            create_shortcut_link.json()['id']
        ),
        allow_redirects=False
    )
    assert response.headers['Location'] == URL, (
        'Expected redirect location is {expected}, got {actual}'.format(
            expected=URL, actual=response.headers['Location']
        )
    )


@allure.feature('Redirect service')
@allure.story('Valid request response body')
def test_redirect_body(
        purge_all_links, create_shortcut_link
):
    response = requests.get(
        url='http://localhost:8888/r/{}'.format(
            create_shortcut_link.json()['id']
        ),
        allow_redirects=False
    )
    assert response.text == '302: Found', (
        'Expected response body is "302: Found", got {actual}'.format(
            actual=response.text
        )
    )


@allure.feature('Redirect service')
@allure.story('Invalid method status code')
def test_redirect_wrong_method_status_code(
        purge_all_links, create_shortcut_link
):
    response = requests.post(
        url='http://localhost:8888/r/{}'.format(
            create_shortcut_link.json()['id']
        ),
        data='{}'
    )
    assert response.status_code == 405, (
        'Expected status code is 405, got {actual}'.format(
            actual=response.status_code
        )
    )


@allure.feature('Redirect service')
@allure.story('Invalid method response body')
def test_redirect_wrong_method_body(
        purge_all_links, create_shortcut_link
):
    response = requests.post(
        url='http://localhost:8888/r/{}'.format(
            create_shortcut_link.json()['id']
        ),
        data='{}'
    )

    v = Validator(
        {
            'status': {'type': 'integer', 'allowed': [405]},
            'message': {'type': 'string', 'allowed': ['Method Not Allowed']}
        }
    )
    assert v.validate(response.json()), v.errors


@allure.feature('Redirect service')
@allure.story('Invalid link ID status code')
def test_redirect_invalid_id_status_code(purge_all_links):
    response = requests.get(
        url='http://localhost:8888/r/{}'.format(uuid.uuid4())
    )
    assert response.status_code == 404, (
        'Expected status code is 404, got {actual}'.format(
            actual=response.status_code
        )
    )


@allure.feature('Redirect service')
@allure.story('Invalid link ID response body')
def test_redirect_invalid_id_body(purge_all_links):
    response = requests.get(
        url='http://localhost:8888/r/{}'.format(uuid.uuid4())
    )

    v = Validator(
        {
            'status': {'type': 'integer', 'allowed': [404]},
            'message': {'type': 'string', 'allowed': ['Not Found']}
        }
    )
    assert v.validate(response.json()), v.errors
