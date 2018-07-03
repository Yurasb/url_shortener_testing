from hamcrest.core.base_matcher import BaseMatcher
from cerberus import Validator


class SchemaValidator(BaseMatcher):
    def __init__(self, schema):
        self.schema = schema

    def _matches(self, item):
        if not isinstance(item, dict):
            return False
        v = Validator(self.schema)
        return v.validate(item)

    def describe_to(self, description):
        description.append_text('{}'.format(self.schema))


def match_to(schema):
    return SchemaValidator(schema)
