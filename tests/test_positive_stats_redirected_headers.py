import requests


def test_positive_stats_redirected_headers(url, test_case):
    response = requests.post(url, data=test_case.id_data)
    assert response.headers == test_case.exp_headers
