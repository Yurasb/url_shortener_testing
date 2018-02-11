from lxml import html

import requests
from cerberus import Validator


def test_delete_all_links_status_code(create_shortcut_link):
    response = requests.delete(
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    assert response.status_code == 200


def test_delete_all_links_removed(create_shortcut_link):
    requests.delete(
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )

    check = requests.get(
        url='http://localhost:8888/admin/all_links'
    )
    v = Validator({'links': {}})
    assert v.validate(check.json()), v.errors


def test_delete_all_links_wrong_method_status_code():
    response = requests.post(
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    assert response.status_code == 405


def test_delete_all_links_wrong_method_body():
    response = requests.post(
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )

    v = Validator(
        {
            'status': {'type': 'integer', 'allowed': [405]},
            'message': {
                'type': 'string', 'allowed': ['Method Not Allowed']
            }
        }
    )
    assert v.validate(response.json()), v.errors


def test_delete_all_links_no_confirmation_status_code():
    response = requests.delete(
        url='http://localhost:8888/admin/all_links'
    )
    assert response.status_code == 500


def test_delete_all_links_no_confirmation_body():
    response = requests.delete(
        url='http://localhost:8888/admin/all_links'
    )

    parsed = html.fromstring(response.text)
    assert parsed.text_content()[:25] == '500 Internal Server Error'
