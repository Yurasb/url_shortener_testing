import yaml


class DataProvider:

    @staticmethod
    def provide_config_for(protocol):
        with open('../data/{protocol}_config.yml'.format(protocol=protocol), 'r') as stream:
            config = yaml.load(stream)
            return config

    @staticmethod
    def provide_test_data_by_id(id):
        with open('../data/test_data.yml', 'r') as stream:
            test_data = yaml.load(stream)
            return test_data[id]

    @staticmethod
    def provide_expected_schema_by_id(id):
        with open('../data/schemas.yml', 'r') as stream:
            schemas = yaml.load(stream)
            return schemas[id]
