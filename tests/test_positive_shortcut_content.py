import requests

from tests import is_content_valid


def test_positive_shortcut_content(url, test_case):
    response = requests.post(url, data=test_case.link_data)
    assert is_content_valid(test_case.scheme, response.content)
