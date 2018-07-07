import yaml


def config():
    with open(
            '/home/yury/PycharmProjects/url_shortener_testing/client_cfg.yml', 'r') as stream:
        config_data = yaml.load(stream)
        return config_data


BASE_URL = '{0}:{1}'.format(config()['host'], config()['port'])
