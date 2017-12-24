import requests


def test_positive_redirect_headers(url, test_case):
    response = requests.get('{}{}'.format(url, test_case.id))
    assert response.headers == test_case.exp_headers
