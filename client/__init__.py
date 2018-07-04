import yaml


def config():
    with open('../client_cfg.yml', 'r') as stream:
        config_data = yaml.load(stream)
        return config_data


class NetworkConfig:
    def __init__(self):
        self.__host = config()['host']
        self.__port = config()['port']
        self.__base_url = self.base_url

    @property
    def base_url(self):
        return '{0}:{1}'.format(self.__host, self.__port)

    def __str__(self):
        return self.__base_url


BASE_URL = NetworkConfig()
