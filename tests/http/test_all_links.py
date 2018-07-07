import allure
from hamcrest import assert_that

from client import http
from data import schemas, payloads
from tests.matchers import match_to


@allure.feature('All links handler')
@allure.story('HTTP GET when DB is empty')
def test_http_valid_payload_when_db_is_empty():
    response = http.all_links(method='GET')
    assert_that(response, match_to(schemas.ALL_LINKS_EMPTY_DB_POSITIVE))


@allure.feature('All links handler')
@allure.story('HTTP DELETE with Confirmation')
def test_http_valid_payload(create_shortcut_link):
    response = http.all_links(method='DELETE', payload=payloads.PURGE_POSITIVE)
    assert_that(response, match_to(schemas.PURGE_POSITIVE))
