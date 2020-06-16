class TinyUrl:
    def __init__(self):
        self.dict = {}

    def get_short_url(self, url):
        return url[-6:]

    def long_to_short(self, long):
