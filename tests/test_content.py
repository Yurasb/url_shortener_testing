from requests import request

from tests import is_json_content_valid


def test_content(test_case, url):
    response = request(test_case.method, url, data=test_case.data)
    assert is_json_content_valid(test_case.exp_scheme, response.json())
