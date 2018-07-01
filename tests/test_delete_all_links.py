import allure
from hamcrest import assert_that

from data import payloads, schemas
from logic.validation import match_to
from network.client import purge_all_links_by_http, purge_all_links_by_ws


@allure.feature('Delete handler')
@allure.story('Valid HTTP request')
def test_valid_http_request(create_shortcut_link):
    actual_response = purge_all_links_by_http(payloads.VALID_PURGE_PAYLOAD)
    assert_that(actual_response, match_to(schemas.VALID_PURGE_RESPONSE))


@allure.feature('Delete handler')
@allure.story('Valid WebSocket request')
def test_valid_ws_request(create_shortcut_link):
    actual_response = purge_all_links_by_ws(payloads.VALID_PURGE_PAYLOAD)
    assert_that(actual_response, match_to(schemas.VALID_PURGE_RESPONSE))
