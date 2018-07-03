import json
import websocket

from client import BASE_URL


def create_shortcut(payload=None):
    connection = websocket.create_connection('ws://{}/ws'.format(BASE_URL))
    connection.send(json.dumps({'command': 'shortcut', 'body': payload}))
    response = connection.recv()
    connection.close()
    return json.loads(response)


def purge_all_links(payload=None):
    connection = websocket.create_connection('ws://{}/ws'.format(BASE_URL))
    connection.send(json.dumps({'command': 'purge_all', 'body': payload}))
    response = connection.recv()
    connection.close()
    return json.loads(response)


def get_all_links():
    connection = websocket.create_connection('ws://{}/ws'.format(BASE_URL))
    connection.send(json.dumps({'command': 'get_all_links', 'body': {}}))
    response = connection.recv()
    connection.close()
    return json.loads(response)