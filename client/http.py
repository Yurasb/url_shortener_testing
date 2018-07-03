from requests import request

from client import BASE_URL


def create_shortcut(payload=None):
    response = request(
        url='http://{}/shortcut'.format(BASE_URL),
        method='POST',
        json=payload
    )
    return {'code': response.status_code, 'body': response.json()}


def purge_all_links(payload=None):
    response = request(
        url='http://{}/admin/all_links'.format(BASE_URL),
        method='DELETE',
        json=payload
    )
    return {'code': response.status_code, 'body': response.json()}


def get_all_links():
    response = request(
        url='http://{}/admin/all_links'.format(BASE_URL),
        method='GET'
    )
    return {'code': response.status_code, 'body': response.json()}
