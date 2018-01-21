import json


class CreateLinkRequest:
    @staticmethod
    def from_link(link):
        return json.dumps({'link': link})
