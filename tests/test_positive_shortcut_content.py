import requests


def test_positive_shortcut_content(url, test_case):
    response = requests.post(url, data=test_case.link_data)
    assert response.content == test_case.exp_content
