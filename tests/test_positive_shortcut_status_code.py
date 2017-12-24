import requests


def test_positive_shortcut_status_code(url, test_case):
    response = requests.post(url, data=test_case.link_data)
    assert response.status_code == test_case.exp_status_code
