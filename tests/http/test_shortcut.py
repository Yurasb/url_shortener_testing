import allure
from hamcrest import assert_that

from client import http
from data import payloads, schemas
from tests.matchers import match_to


@allure.feature('Shortcut handler')
@allure.story('HTTP Valid payload')
def test_http_valid_payload():
    response = http.create_shortcut(payload=payloads.SHORTCUT_POSITIVE)
    assert_that(response, match_to(schemas.SHORTCUT_POSITIVE))
