class HTTPTestCase:
    def __init__(self, data):
        self.method = data['method']
        self.payload = data['payload']

    def __str__(self):
        return 'Query {method} with body {payload}'.format(method=self.method, payload=self.payload)


class WSTestCase:
    def __init__(self, data):
        self.command = data['command']
        self.payload = data['body']

    def __str__(self):
        return 'WS {command} with payload {payload}'.format(command=self.command, payload=self.payload)
