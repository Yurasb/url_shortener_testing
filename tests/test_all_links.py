import allure
from hamcrest import assert_that

from client import http, ws
from data import schemas
from tests.matchers import match_to


@allure.feature('All links handler')
@allure.story('HTTP Valid payload when DB is empty')
def test_http_valid_payload_when_db_is_empty():
    response = http.get_all_links()
    assert_that(response, match_to(schemas.VALID_ALL_LINKS_EMPTY_LIST_RESPONSE))


@allure.feature('All links handler')
@allure.story('WebSocket request when DB is empty')
def test_ws_valid_payload_when_db_is_empty():
    response = ws.get_all_links()
    assert_that(response, match_to(schemas.VALID_ALL_LINKS_EMPTY_LIST_RESPONSE))
