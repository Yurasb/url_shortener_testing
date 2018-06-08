import allure
from hamcrest import assert_that, equal_to

from logic.validation import match_to


URL = 'https://github.com/Yurasb/url_shortener_testing'


@allure.feature('Shortcut handler')
@allure.story('Valid HTTP request')
def test_shortcut_status_code(http_client, test_context, expected_schema):
    client = http_client
    actual_response = client.create_shortcut(test_context)
    assert_that(actual_response.status_code, equal_to(200), 'status code')
    assert_that(actual_response.json(), match_to(expected_schema), 'response body')


# @allure.feature('Shortcut handler')
# @allure.story('Valid request response body')
# def test_shortcut_body():
#     response = requests.post(
#         url='http://localhost:8888/shortcut',
#         json=dict(link=URL)
#     )
#
#     v = Validator(
#         dict(id=dict(type='string', allowed=[response.json()['id']]))
#     )
#     assert v.validate(response.json()), v.errors
#
#
# @allure.feature('Shortcut handler')
# @allure.story('Valid WebSocket query')
# def test_ws_shortcut_valid_query(ws_connection):
#     ws_connection.send(json.dumps(
#         dict(command='shortcut',
#              body=dict(link='https://github.com/Yurasb/url_shortener_testing'))
#     ))
#     response = ws_connection.recv()
#
#     check = requests.get(
#         url='http://localhost:8888/admin/all_links'
#     )
#     v = Validator(
#         dict(code=dict(type='integer', allowed=[200]),
#              body=dict(type='dict', schema=dict(
#                  id=dict(type='string', allowed=list(
#                      check.json()['links'].keys()
#                  )))))
#     )
#     assert v.validate(json.loads(response)), v.errors
#
#
# @allure.feature('Shortcut handler')
# @allure.story('Check if shortcut is created')
# def test_shortcut_created():
#     requests.post(
#         url='http://localhost:8888/shortcut',
#         json=dict(link=URL)
#     )
#
#     check = requests.get(
#         url='http://localhost:8888/admin/all_links'
#     )
#     assert URL in json.dumps(check.json()), (
#         '{url} is not found in shortcut list'.format(url=URL)
#     )
#
#
# @allure.feature('Shortcut handler')
# @allure.story('Invalid method status code')
# def test_shortcut_wrong_method_status_code():
#     response = requests.get(
#         url='http://localhost:8888/shortcut'
#     )
#     assert response.status_code == 405, (
#         'Expected status code is 405, got {actual}'.format(
#             actual=response.status_code
#         )
#     )
#
#
# @allure.feature('Shortcut handler')
# @allure.story('Invalid method response body')
# def test_shortcut_wrong_method_body():
#     response = requests.get(
#         url='http://localhost:8888/shortcut'
#     )
#
#     v = Validator(
#         dict(status=dict(type='integer', allowed=[405]),
#              message=dict(type='string', allowed=['Method Not Allowed']))
#     )
#     assert v.validate(response.json()), v.errors
#
#
# @allure.feature('Shortcut handler')
# @allure.story('Invalid JSON data status code')
# def test_shortcut_invalid_json_status_code():
#     response = requests.post(
#         url='http://localhost:8888/shortcut',
#         data='{ "link" "https://github.com/Yurasb/url_shortener_testing"}'
#     )
#     assert response.status_code == 406, (
#         'Expected status code is 406, got {actual}'.format(
#             actual=response.status_code
#         )
#     )
#
#
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
