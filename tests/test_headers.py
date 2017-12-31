from requests import request


def test_headers_content_length(url, test_case):
    response = request(test_case.method, url, data=test_case.data)
    assert response.headers['Content-Length'] == test_case.exp_headers['Content-Length']


def test_headers_content_type(url, test_case):
    response = request(test_case.method, url, data=test_case.data)
    assert response.headers['Content-Type'] == test_case.exp_headers['Content-Type']


def test_date_in_headers(url, test_case):
    response = request(test_case.method, url, data=test_case.data)
    assert 'Date' in response.headers
