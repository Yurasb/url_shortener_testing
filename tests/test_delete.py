import allure
from hamcrest import assert_that

from client import http, ws
from data import payloads, schemas
from tests.matchers import match_to


@allure.feature('Delete handler')
@allure.story('HTTP Valid payload')
def test_http_valid_payload(create_shortcut_link):
    response = http.purge_all_links(payloads.VALID_PURGE_PAYLOAD)
    assert_that(response, match_to(schemas.VALID_PURGE_RESPONSE))


@allure.feature('Delete handler')
@allure.story('Valid WebSocket request')
def test_ws_valid_payload(create_shortcut_link):
    response = ws.purge_all_links(payloads.VALID_PURGE_PAYLOAD)
    assert_that(response, match_to(schemas.VALID_PURGE_RESPONSE))
