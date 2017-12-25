class TestCase(object):
    def __init__(self, link_data, exp_status_code):
        self.link_data = link_data
        self.exp_status_code = exp_status_code

positive_shortcut = TestCase(
    link_data=u'{"link": "https://github.com/Yurasb/url_shortener_testing"}',
    exp_status_code=200
)
