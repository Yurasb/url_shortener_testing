class TestCase(object):
    def __init__(self, method, link_data, exp_scheme, exp_status_code):
        self.method = method
        self.link_data = link_data
        self.exp_scheme = exp_scheme
        self.exp_status_code = exp_status_code

positive_shortcut = TestCase(
    method='POST',
    link_data=u'{"link": "https://github.com/Yurasb/url_shortener_testing"}',
    exp_scheme={'id': {'type': 'string'}},
    exp_status_code=200
)

positive_stats_new = TestCase(
    method='POST',
    link_data=u'{"id": "a6b6d734-8e73-4179-aa8b-8a7994eaa691"}',
    exp_scheme={'last_redirected': {'nullable': True, 'type': 'datetime'}, 'redirects_count': {'type': 'integer'}},
    exp_status_code=200
)

TEST_SUITE = [positive_shortcut, positive_stats_new]
