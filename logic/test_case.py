class TestCase:
    def __init__(self, data):
        self.method = data['method']
        self.payload = None or data['payload']

    def __str__(self):
        return 'Query {method} with payload {payload}'.format(method=self.method, payload=self.payload)
