import requests


def test_positive_shortcut_headers(url, test_case):
    response = requests.post(url, data=test_case.link_data)
    assert response.headers == test_case.exp_headers
