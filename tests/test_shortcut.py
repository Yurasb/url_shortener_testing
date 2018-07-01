import allure
from hamcrest import assert_that, equal_to

from data import schemas, payloads
from logic.validation import match_to
from network.client import create_shortcut_by_http, create_shortcut_by_ws


@allure.feature('Shortcut handler')
@allure.story('Valid HTTP request')
def test_http_shortcut_valid_request(http_client, test_context, expected_schema):
    client = http_client
    actual_response = client.create_shortcut(test_context)
    assert_that(actual_response.status_code, equal_to(200), 'status code')
    assert_that(actual_response.json(), match_to(expected_schema), 'response body')


@allure.feature('Shortcut handler')
@allure.story('Valid WebSocket request')
def test_ws_shortcut_valid_request(ws_client, ws_test_context, expected_schema):
    client = ws_client
    actual_response = client.create_shortcut(ws_test_context)
    assert_that(actual_response['code'], equal_to(200), 'status code')
    assert_that(actual_response['body'], match_to(schemas.VALID_SHORTCUT_RESPONSE), 'response body')
