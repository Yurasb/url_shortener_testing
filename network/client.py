import json
import websocket
from requests import request

from network import NetworkConfig


BASE_URL = NetworkConfig()


def create_shortcut_by_http(payload=None):
    response = request(
        url='http://{}/shortcut'.format(BASE_URL),
        method='POST',
        json=payload
    )
    return {'code': response.status_code, 'body': response.json()}


def create_shortcut_by_ws(payload=None):
    connection = websocket.create_connection('ws://{}/ws'.format(BASE_URL))
    connection.send(json.dumps({'command': 'shortcut', 'body': payload}))
    response = connection.recv()
    connection.close()
    return json.loads(response)


def purge_all_links_by_http(payload=None):
    response = request(
        url='http://{}/admin/all_links'.format(BASE_URL),
        method='DELETE',
        json=payload
    )
    return {'code': response.status_code, 'body': response.json()}


def purge_all_links_by_ws(payload=None):
    connection = websocket.create_connection('ws://{}/ws'.format(BASE_URL))
    connection.send(json.dumps({'command': 'purge_all', 'body': payload}))
    response = connection.recv()
    connection.close()
    return json.loads(response)
