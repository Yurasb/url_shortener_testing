from cerberus import Validator
from requests import request


def test_delete_all_links_status_code():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    request(
        method='POST',
        url='http://localhost:8888/shortcut',
        data='{ "link": "https://github.com/Yurasb/url_shortener_testing"}'
    )
    # action
    response = request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # validation
    assert response.status_code == 200


def test_delete_all_links_removed():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    request(
        method='POST',
        url='http://localhost:8888/shortcut',
        data='{ "link": "https://github.com/Yurasb/url_shortener_testing"}'
    )
    # action
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # validation - to be completed with JSON-schema
    check = request(
        method='GET',
        url='http://localhost:8888/admin/all_links'
    )
    v = Validator()
    assert v.validate(check.json())


def test_delete_all_links_wrong_method():
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # validation
    assert response.status_code == 406


def test_delete_all_links_no_confirmation():
    # action
    response = request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links'
    )
    # validation
    assert response.status_code == 400
