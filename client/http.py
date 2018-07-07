from requests import request

from client import BASE_URL


def create_shortcut(**kwargs):
    if 'method' not in kwargs:
        response = request(
            url='http://{}/shortcut'.format(BASE_URL),
            method='POST',
            json=kwargs['payload']
        )
    else:
        response = request(
            url='http://{}/shortcut'.format(BASE_URL),
            method=kwargs['method'],
            json=kwargs['payload']
        )
    return {'code': response.status_code, 'body': response.json()}


def all_links(**kwargs):
    if not kwargs:
        response = request(
            url='http://{}/admin/all_links'.format(BASE_URL),
            method='GET',
            json=None
        )
    else:
        response = request(
            url='http://{}/admin/all_links'.format(BASE_URL),
            method=kwargs['method'],
            json=kwargs['payload']
        )
    return {'code': response.status_code, 'body': response.json()}
