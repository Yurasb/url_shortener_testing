import allure
from hamcrest import assert_that

from client import http, ws
from data import payloads, schemas
from tests.matchers import match_to


@allure.feature('Shortcut handler')
@allure.story('HTTP Valid payload')
def test_http_valid_payload():
    response = http.create_shortcut(payloads.VALID_SHORTCUT_PAYLOAD)
    assert_that(response, match_to(schemas.VALID_SHORTCUT_RESPONSE))


@allure.feature('Shortcut handler')
@allure.story('WS Valid payload')
def test_ws_valid_payload():
    actual_response = ws.create_shortcut(payloads.VALID_SHORTCUT_PAYLOAD)
    assert_that(actual_response, match_to(schemas.VALID_SHORTCUT_RESPONSE))
