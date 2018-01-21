class LinkContext:
    def __init__(self, link, link_id=None, redirect_count=None, redirect_at=None):
        self.link = link
        self.link_id = link_id
        self.redirect_count = redirect_count
        self.redirect_at = redirect_at
