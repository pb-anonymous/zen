from collections import OrderedDict

class LinkList:
    def __init__(self):
        self.links = OrderedDict()

    def add(self, link):
        self.links[link] = None

    def get_links(self):
        return list(self.links.keys())
