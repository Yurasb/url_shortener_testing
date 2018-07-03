VALID_SHORTCUT_RESPONSE = {
    'code': {
        'type': 'integer',
        'allowed': [200]
    },
    'body': {
        'type': 'dict',
        'schema': {
            'id': {
                'type': 'string',
                'empty': False,
                'minlength': 10,
                'maxlength': 10
            }
        }
    }
}
VALID_PURGE_RESPONSE = {
    'code': {
        'type': 'integer',
        'allowed': [200]
    },
    'body': {'empty': True}
}
VALID_ALL_LINKS_EMPTY_LIST_RESPONSE = {
    'code': {
        'type': 'integer',
        'allowed': [200]
    },
    'body': {
        'type': 'dict',
        'schema': {
            'links': {'empty': True}
        }
    }
}