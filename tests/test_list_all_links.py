import requests

from cerberus import Validator


def test_list_all_links_empty_status_code(purge_all_links):
    # precondition
    purge_all_links
    # action
    response = requests.get(
        url='http://localhost:8888/admin/all_links'
    )
    # validation
    assert response.status_code == 200


def test_list_all_links_empty_body(purge_all_links):
    # precondition
    purge_all_links
    # action
    response = requests.get(
        url='http://localhost:8888/admin/all_links'
    )
    # validation
    v = Validator({'links': {}})
    assert v.validate(response.json()), v.errors


def test_list_all_links_not_empty_status_code(
        purge_all_links, create_shortcut_link
):
    # precondition
    purge_all_links
    create_shortcut_link
    # action
    response = requests.get(
        url='http://localhost:8888/admin/all_links'
    )
    # validation
    assert response.status_code == 200


def test_list_all_links_not_empty_body(
        purge_all_links, create_shortcut_link
):
    # precondition
    purge_all_links
    create_shortcut_link
    # action
    response = requests.get(
        url='http://localhost:8888/admin/all_links'
    )
    # validation
    v = Validator(
        {
            'links': {
                'type': 'dict', 'schema': {
                    str(create_shortcut_link.json()['id']): {
                        'type': 'string',
                        'allowed': ['https://github.com/Yurasb/url_shortener_testing']
                    }
                }
            }
        }
    )
    assert v.validate(response.json()), v.errors


def test_list_all_links_wrong_method_status_code():
    # action
    response = requests.post(
        url='http://localhost:8888/admin/all_links',
        data='{}'
    )
    # validation
    assert response.status_code == 405


def test_all_links_wrong_method_body():
    # action
    response = requests.post(
        url='http://localhost:8888/admin/all_links',
        data='{}'
    )
    # validation
    v = Validator(
        {
            'status': {'type': 'integer', 'allowed': [405]},
            'message': {
                'type': 'string', 'allowed': ['Method Not Allowed']
            }
        }
    )
    assert v.validate(response.json()), v.errors
