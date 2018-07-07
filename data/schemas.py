SHORTCUT_POSITIVE = {
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
PURGE_POSITIVE = {
    'code': {
        'type': 'integer',
        'allowed': [200]
    },
    'body': {'empty': True}
}
ALL_LINKS_EMPTY_DB_POSITIVE = {
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
