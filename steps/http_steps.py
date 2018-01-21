import requests

from conf.http import CreateLinkRequest


def create_link(link, method='POST'):
    return requests.request(
        method=method,
        url='http://localhost:8888/shortcut',
        data=CreateLinkRequest.from_link(link)
    )


def get_all_links():
    return requests.get(
        'http://localhost:8888/admin/all_links'
    )
