class TestCase(object):
    def __init__(self, method, data, exp_scheme, exp_status_code, exp_headers, exp_encoding):
        self.method = method
        self.data = data
        self.exp_scheme = exp_scheme
        self.exp_status_code = exp_status_code
        self.exp_headers = exp_headers
        self.exp_encoding = exp_encoding

positive_shortcut = TestCase(
    method='POST',
    data=u'{"link": "https://github.com/Yurasb/url_shortener_testing"}',
    exp_scheme={'id': {'type': 'string'}},
    exp_status_code=200,
    exp_headers={'Content-Length': '46', 'Content-Type': 'application/json; charset=utf-8'},
    exp_encoding='utf-8'
)

positive_stats_new = TestCase(
    method='POST',
    data=u'{"id": "a6b6d734-8e73-4179-aa8b-8a7994eaa691"}',
    exp_scheme={'last_redirected': {'nullable': True, 'type': 'datetime'}, 'redirects_count': {'type': 'integer'}},
    exp_status_code=200,
    exp_headers={'Content-Length': '47', 'Content-Type': 'application/json; charset=utf-8'},
    exp_encoding='utf-8'
)

TEST_SUITE = [positive_shortcut, positive_stats_new]
