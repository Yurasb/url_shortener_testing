import allure
from hamcrest import assert_that, equal_to

from logic.validation import match_to


URL = 'https://github.com/Yurasb/url_shortener_testing'


@allure.feature('Shortcut handler')
@allure.story('Valid HTTP request')
def test_http_shortcut_valid_request(http_client, test_context, expected_schema):
    client = http_client
    actual_response = client.create_shortcut(test_context)
    assert_that(actual_response.status_code, equal_to(200), 'status code')
    assert_that(actual_response.json(), match_to(expected_schema), 'response body')


@allure.feature('Shortcut handler')
@allure.story('Valid WebSocket request')
def test_ws_shortcut_valid_request(ws_client, ws_test_context, expected_schema):
    client = ws_client
    actual_response = client.create_shortcut(ws_test_context)
    assert_that(actual_response['code'], equal_to(200), 'status code')
    assert_that(actual_response['body'], match_to(expected_schema), 'response body')


@allure.feature('Shortcut handler')
@allure.story('Invalid query with GET method')
def test_http_shortcut_with_get(http_client, test_context, expected_schema):
    client = http_client
    actual_response = client.create_shortcut(test_context)
    assert_that(actual_response.status_code, equal_to(405), 'status code')
    assert_that(actual_response.json(), match_to(expected_schema), 'response body')


# getting 500 Internal Server Error instead of expected 406 and message
@allure.feature('Shortcut handler')
@allure.story('Invalid query with bad payload')
def test_http_shortcut_with_bad_payload(http_client, test_context, expected_schema):
    client = http_client
    actual_response = client.create_shortcut(test_context)
    assert_that(actual_response.status_code, equal_to(406), 'status code')
    assert_that(actual_response.json(), match_to(expected_schema), 'response body')


# @allure.feature('Shortcut handler')
# @allure.story('Invalid JSON data response body')
# def test_shortcut_invalid_json_body():
#     response = requests.post(
#         url='http://localhost:8888/shortcut',
#         data='{ "link" "https://github.com/Yurasb/url_shortener_testing"}'
#     )
#
#     v = Validator(
#         dict(message=dict(type='string', allowed=['Invalid json']),
#              status=dict(type='integer', allowed=[406]))
#     )
#     assert v.validate(response.json()), v.errors
#
#
# @allure.feature('Shortcut handler')
# @allure.story('WebSocket query with invalid JSON data')
# def test_ws_shortcut_invalid_json(ws_connection):
#     ws_connection.send(json.dumps(
#         dict(command='shortcut', body='https://github.com/Yurasb/url_shortener_testing')
#     ))
#     response = ws_connection.recv()
#
#     v = Validator(
#         dict(code=dict(type='integer', allowed=[400]),
#              error=dict(type='dict', schema=dict(
#                  body=dict(type='list', allowed=['must be of dict type'])
#              )))
#     )
#     assert v.validate(json.loads(response)), v.errors
#
#
# @allure.feature('Shortcut handler')
# @allure.story('Invalid URL status code')
# def test_shortcut_invalid_link():
#     response = requests.post(
#         url='http://localhost:8888/shortcut',
#         json=dict(link='github.com/Yurasb/url_shortener_testing')
#     )
#     assert response.status_code == 400, (
#         'Expected status code is 400, got {actual}'.format(
#             actual=response.status_code
#         )
#     )
#
#
# @allure.feature('Shortcut handler')
# @allure.story('WebSocket query with invalid link')
# def test_ws_shortcut_invalid_link(ws_connection):
#     ws_connection.send(json.dumps(
#         dict(command='shortcut',
#              body=dict(link='github.com/Yurasb/url_shortener_testing'))
#     ))
#     response = ws_connection.recv()
#
#     v = Validator(
#         dict(code=dict(type='integer', allowed=[400]),
#              error=dict(type='dict', schema=dict(
#                  link=dict(type='list', allowed=[(
#                      "value does not match regex "
#                      "'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|"
#                      "(?:%[0-9a-fA-F][0-9a-fA-F]))+'"
#                  )]))))
#     )
#     assert v.validate(json.loads(response)), v.errors
