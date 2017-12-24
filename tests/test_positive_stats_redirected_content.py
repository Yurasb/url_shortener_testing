import requests


def test_positive_stats_redirected_content(url, test_case):
    response = requests.post(url, data=test_case.id_data)
    assert response.content == test_case.exp_content
