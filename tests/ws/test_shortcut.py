import allure
from hamcrest import assert_that

from client import ws
from data import payloads, schemas
from tests.matchers import match_to


@allure.feature('Shortcut handler')
@allure.story('WS Valid payload')
def test_ws_valid_payload():
    actual_response = ws.create_shortcut(payload=payloads.SHORTCUT_POSITIVE)
    assert_that(actual_response, match_to(schemas.SHORTCUT_POSITIVE))
