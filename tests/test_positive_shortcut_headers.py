import requests


def test_positive_shortcut_headers_content_length(url, test_case):
    response = requests.post(url, data=test_case.link_data)
    assert response.headers['Content-Length'] == '46'


def test_positive_shortcut_headers_content_type(url, test_case):
    response = requests.post(url, data=test_case.link_data)
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'


def test_positive_shortcut_headers_date(url, test_case):
    response = requests.post(url, data=test_case.link_data)
    assert 'Date' in response.headers
