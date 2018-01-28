from cerberus import Validator
from requests import request


def test_delete_all_links_status_code(create_shortcut_link):
    # precondition
    create_shortcut_link
    # action
    response = request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # validation
    assert response.status_code == 200


def test_delete_all_links_removed(create_shortcut_link):
    # precondition
    create_shortcut_link
    # action
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # validation
    check = request(
        method='GET',
        url='http://localhost:8888/admin/all_links'
    )
    v = Validator({'links': {}})
    assert v.validate(check.json())


def test_delete_all_links_wrong_method_status_code():
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # validation
    assert response.status_code == 405


def test_delete_all_links_wrong_method_body():
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
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
    assert v.validate(response.json())


def test_delete_all_links_no_confirmation_status_code():
    # action
    response = request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links'
    )
    # validation
    assert response.status_code == 500


def test_delete_all_links_no_confirmation_body():
    # action
    response = request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links'
    )
    # validation - to be completed with XML-schema
    assert response.content
