from cerberus import Validator
from requests import request


def test_shortcut_status_code():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/shortcut',
        data='{ "link": "https://github.com/Yurasb/url_shortener_testing"}'
    )
    # validation
    assert response.status_code == 200


def test_shortcut_body():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/shortcut',
        data='{ "link": "https://github.com/Yurasb/url_shortener_testing"}'
    )
    # validation
    v = Validator({'id': {'type': 'string'}})
    assert v.validate(response.json())


def test_shortcut_created():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # action
    request(
        method='POST',
        url='http://localhost:8888/shortcut',
        data='{ "link": "https://github.com/Yurasb/url_shortener_testing"}'
    )
    # validation
    check = request(
        method='GET',
        url='http://localhost:8888/admin/all_links'
    )
    assert "https://github.com/Yurasb/url_shortener_testing" in check.json()


def test_shortcut_wrong_method():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # action
    response = request(
        method='GET',
        url='http://localhost:8888/shortcut'
    )
    # validation
    assert response.status_code == 406


def test_shortcut_invalid_json():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/shortcut',
        data='{ "link" "https://github.com/Yurasb/url_shortener_testing"}'
    )
    # validation
    assert response.status_code == 400


def test_shortcut_invalid_link():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/shortcut',
        data='{ "link": "github.com/Yurasb/url_shortener_testing"}'
    )
    # validation
    assert response.status_code == 400
