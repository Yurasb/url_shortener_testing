import uuid

from cerberus import Validator
from requests import request

from data import get_xmlschema
from tests import parse_html


def test_redirect_status_code(purge_all_links, create_shortcut_link):
    # precondition
    purge_all_links
    create_shortcut_link
    # action
    response = request(
        method='GET',
        url='http://localhost:8888/r/{}'.format(
            create_shortcut_link.json()['id']
        )
    )
    # validation
    assert response.status_code == 302


def test_redirect_is_redirect(purge_all_links, create_shortcut_link):
    # precondition
    purge_all_links
    create_shortcut_link
    # action
    response = request(
        method='GET',
        url='http://localhost:8888/r/{}'.format(
            create_shortcut_link.json()['id']
        )
    )
    # validation
    assert response.is_redirect


def test_redirect_body(purge_all_links, create_shortcut_link):
    # precondition
    purge_all_links
    create_shortcut_link
    # action
    response = request(
        method='GET',
        url='http://localhost:8888/r/{}'.format(
            create_shortcut_link.json()['id']
        )
    )
    # validation
    parsed_body = parse_html(response.text)
    xmlschema = get_xmlschema()
    xmlschema.assertValid(parsed_body)


def test_redirect_wrong_method_status_code(purge_all_links, create_shortcut_link):
    # precondition
    purge_all_links
    create_shortcut_link
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/r/{}'.format(
            create_shortcut_link.json()['id']
        ),
        data='{}'
    )
    # validation
    assert response.status_code == 405


def test_redirect_wrong_method_body(purge_all_links, create_shortcut_link):
    # precondition
    purge_all_links
    create_shortcut_link
    # action
    response = request(
        method='POST',
        url='http://localhost:8888/r/{}'.format(
            create_shortcut_link.json()['id']
        ),
        data='{}'
    )
    # validation
    v = Validator(
        {
            'status': {'type': 'integer', 'allowed': [405]},
            'message': {'type': 'string', 'allowed': ['Method Not Allowed']}
        }
    )
    assert v.validate(response.json())


def test_redirect_invalid_id_status_code(purge_all_links):
    # precondition
    purge_all_links
    # action
    response = request(
        method='GET',
        url='http://localhost:8888/r/{}'.format(uuid.uuid4())
    )
    # validation
    assert response.status_code == 404


def test_redirect_invalid_id_body(purge_all_links):
    # precondition
    purge_all_links
    # action
    response = request(
        method='GET',
        url='http://localhost:8888/r/{}'.format(uuid.uuid4())
    )
    # validation
    v = Validator(
        {
            'status': {'type': 'integer', 'allowed': [404]},
            'message': {'type': 'string', 'allowed': ['Not Found']}
        }
    )
    assert v.validate(response.json())
