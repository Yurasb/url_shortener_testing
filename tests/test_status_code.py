from requests import request


def test_status_code(url, test_case):
    response = request(test_case.method, url, data=test_case.data)
    assert response.status_code == test_case.exp_status_code
