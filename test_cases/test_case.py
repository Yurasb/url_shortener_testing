class TestCase(object):
    def __init__(self, link_data, scheme, exp_status_code):
        self.link_data = link_data
        self.scheme = scheme
        self.exp_status_code = exp_status_code

positive_shortcut = TestCase(
    link_data=u'{"link": "https://github.com/Yurasb/url_shortener_testing"}',
    scheme={'id': {'type': 'string'}},
    exp_status_code=200
)
