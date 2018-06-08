from requests import request


class HTTPClient:
    def __init__(self, config):
        self.__host = config['host']
        self.__port = config['port']
        self.__app_url = self.app_url

    @property
    def app_url(self):
        return 'http://{host}:{port}'.format(host=self.__host, port=self.__port)

    def create_shortcut(self, test_data):
        response = request(
            url='{base_url}/shortcut'.format(base_url=self.app_url),
            method=test_data.method,
            json=test_data.payload
        )
        return response

    def __str__(self):
        return self.__app_url
