import requests


def test_positive_redirect_content(url, test_case):
    response = requests.get('{}{}'.format(url, test_case.id))
    assert response.content == test_case.exp_content
