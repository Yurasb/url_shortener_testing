import allure
from hamcrest import assert_that

from client import ws
from data import schemas, payloads
from tests.matchers import match_to


@allure.feature('All links handler')
@allure.story('WebSocket GET when DB is empty')
def test_ws_valid_payload_when_db_is_empty():
    response = ws.get_all_links()
    assert_that(response, match_to(schemas.ALL_LINKS_EMPTY_DB_POSITIVE))


@allure.feature('All links handler')
@allure.story('WebSocket GET when DB is not empty')
def test_ws_valid_payload_when_db_is_not_empty(create_shortcut):
    response = ws.get_all_links()
    assert_that(response, match_to(schemas.ALL_LINKS_NOT_EMPTY_DB_POSITIVE))


@allure.feature('All links handler')
@allure.story('WebSocket DELETE with Confirmation')
def test_ws_valid_payload(create_shortcut):
    response = ws.purge_all_links(payload=payloads.PURGE_POSITIVE)
    assert_that(response, match_to(schemas.PURGE_POSITIVE))
