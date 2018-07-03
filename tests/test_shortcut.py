import allure
from hamcrest import assert_that, equal_to

from data import payloads, schemas
from logic.validation import match_to
from network.client import create_shortcut_by_http, create_shortcut_by_ws


@allure.feature('Shortcut handler')
@allure.story('Valid HTTP request')
def test_valid_http_request():
    actual_response = create_shortcut_by_http(payloads.VALID_SHORTCUT_PAYLOAD)
    assert_that(actual_response, match_to(schemas.VALID_SHORTCUT_RESPONSE))


@allure.feature('Shortcut handler')
@allure.story('Valid WebSocket request')
def test_valid_ws_request():
    actual_response = create_shortcut_by_ws(payload=payloads.VALID_SHORTCUT_PAYLOAD)
    assert_that(actual_response['code'], equal_to(200), 'status code')
    assert_that(actual_response['body'], match_to(schemas.VALID_SHORTCUT_RESPONSE), 'response body')
