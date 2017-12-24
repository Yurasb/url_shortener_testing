import requests


def test_positive_redirect_status_code(url, test_case):
    response = requests.get('{}{}'.format(url, test_case.id))
    assert response.status_code == test_case.exp_status_code
