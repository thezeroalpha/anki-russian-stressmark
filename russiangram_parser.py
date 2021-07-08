import codecs
from html.parser import HTMLParser

class RussiangramParser(HTMLParser):
    def __init__(self):
        self.intextarea = False
        self.data = ''
        super().__init__()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "textarea" and attrs['id'] == "MainContent_UserSentenceTextbox":
            self.intextarea = True

    def handle_endtag(self, tag):
        if tag == "textarea" and self.intextarea:
            self.intextarea = False

    def handle_data(self, data):
        if self.intextarea:
            bstrings = filter(lambda y: '\\' not in y, data.split('\\x'))
            bs = bytes(map(lambda x: int(x, 16), bstrings))
            self.data = bs.decode()
