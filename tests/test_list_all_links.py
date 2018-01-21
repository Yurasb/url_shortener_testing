from cerberus import Validator
from requests import request


def test_list_all_links_status_code():
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
        method='GET',
        url='http://localhost:8888/admin/all_links'
    )
    # validation
    assert response.status_code == 200


def test_list_all_links_body():
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
        method='GET',
        url='http://localhost:8888/admin/all_links'
    )
    # validation - to be completed with JSON-schema
    v = Validator()
    assert v.validate(response.json())


def test_list_all_links_wrong_method():
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/admin/all_links',
        data='{}'
    )
    # validation
    assert response.status_code == 406
