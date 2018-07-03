import allure
from hamcrest import assert_that

from data import schemas
from logic.validation import match_to
from network.client import get_all_links_by_http, get_all_links_by_ws


@allure.feature('List all links handler')
@allure.story('Valid HTTP request when list is empty')
def test_valid_http_request_when_list_is_empty():
    actual_response = get_all_links_by_http()
    assert_that(actual_response, match_to(schemas.VALID_ALL_LINKS_EMPTY_LIST_RESPONSE))


@allure.feature('List all links handler')
@allure.story('Valid WebSocket request when list is empty')
def test_valid_ws_request_when_list_is_empty():
    actual_response = get_all_links_by_ws()
    assert_that(actual_response, match_to(schemas.VALID_ALL_LINKS_EMPTY_LIST_RESPONSE))
