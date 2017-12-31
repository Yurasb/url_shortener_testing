from cerberus import Validator


def is_json_content_valid(scheme, content):
    v = Validator(scheme)
    return v.validate(content)
