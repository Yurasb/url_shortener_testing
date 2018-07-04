from requests import request

from client import BASE_URL


def create_shortcut(payload=None):
    response = request(
        url='http://{}/shortcut'.format(BASE_URL),
        method='POST',
        json=payload
    )
    return {'code': response.status_code, 'body': response.json()}


def all_links(method=None, payload=None):
    response = request(
        url='http://{}/admin/all_links'.format(BASE_URL),
        method=method,
        json=payload
    )
    return {'code': response.status_code, 'body': response.json()}
