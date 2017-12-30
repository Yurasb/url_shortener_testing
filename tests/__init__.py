import ast

from cerberus import Validator


def is_content_valid(scheme, content):
    v = Validator(scheme)  # validation scheme
    encoded = content.decode('utf-8')  # decode from bytes
    dict_to_validate = ast.literal_eval(encoded)  # convert string to dict
    return v.validate(dict_to_validate)
