import yaml


def config():
    with open('../network/config.yml', 'r') as stream:
        config_data = yaml.load(stream)
        return config_data


def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


@singleton
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
