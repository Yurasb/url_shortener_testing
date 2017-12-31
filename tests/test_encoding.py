from requests import request


def test_encoding(url, test_case):
    response = request(test_case.method, url, data=test_case.data)
    assert response.encoding == test_case.exp_encoding
