# TODO move delete tests here because they're for same handler
# TODO add method parametrization for client(?) with **kwargs
import allure
from hamcrest import assert_that

from client import http, ws
from data import schemas, payloads
from tests.matchers import match_to


@allure.feature('All links handler')
@allure.story('HTTP GET when DB is empty')
def test_http_valid_payload_when_db_is_empty():
    response = http.get_all_links()
    assert_that(response, match_to(schemas.VALID_ALL_LINKS_EMPTY_LIST_RESPONSE))


@allure.feature('All links handler')
@allure.story('WebSocket GET when DB is empty')
def test_ws_valid_payload_when_db_is_empty():
    response = ws.get_all_links()
    assert_that(response, match_to(schemas.VALID_ALL_LINKS_EMPTY_LIST_RESPONSE))


@allure.feature('All links handler')
@allure.story('HTTP DELETE with Confirmation')
def test_http_valid_payload(create_shortcut_link):
    response = http.purge_all_links(payloads.VALID_PURGE_PAYLOAD)
    assert_that(response, match_to(schemas.VALID_PURGE_RESPONSE))


@allure.feature('All links handler')
@allure.story('WebSocket DELETE with Confirmation')
def test_ws_valid_payload(create_shortcut_link):
    response = ws.purge_all_links(payloads.VALID_PURGE_PAYLOAD)
    assert_that(response, match_to(schemas.VALID_PURGE_RESPONSE))
