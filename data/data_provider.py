import yaml


def client_configuration():
    with open('../data/config.yml', 'r') as stream:
        config = yaml.load(stream)
        return config


def test_data_by_id(id):
    with open('../data/test_data.yml', 'r') as stream:
        test_data = yaml.load(stream)
        return test_data[id]


def expected_schema_by_id(id):
    with open('../data/schemas.yml', 'r') as stream:
        schemas = yaml.load(stream)
        return schemas[id]
