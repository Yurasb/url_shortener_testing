import uuid

from requests import request


def test_redirect_status_code():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    create = request(
        method='POST',
        url='http://localhost:8888/shortcut',
        data='{ "link": "https://github.com/Yurasb/url_shortener_testing"}'
    )
    # action
    response = request(
        method='GET',
        url='http://localhost:8888/r/{}'.format(create.json()['id'])
    )
    # validation
    assert response.status_code == 200


def test_redirect_body():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    create = request(
        method='POST',
        url='http://localhost:8888/shortcut',
        data='{ "link": "https://github.com/Yurasb/url_shortener_testing"}'
    )
    # action
    response = request(
        method='GET',
        url='http://localhost:8888/r/{}'.format(create.json()['id'])
    )
    # validation - to be completed using XML-schema
    assert response.content


def test_redirect_wrong_method():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    create = request(
        method='POST',
        url='http://localhost:8888/shortcut',
        data='{ "link": "https://github.com/Yurasb/url_shortener_testing"}'
    )
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/r/{}'.format(create.json()['id']),
        data='{}'
    )
    # validation
    assert response.status_code == 406


def test_redirect_invalid_id():
    # precondition
    request(
        method='DELETE',
        url='http://localhost:8888/admin/all_links',
        data='{"Are you sure?":"Yes"}'
    )
    # action
    response = request(
        method='GET',
        url='http://localhost:8888/r/{}'.format(uuid.uuid4())
    )
    # validation
    assert response.status_code == 400
