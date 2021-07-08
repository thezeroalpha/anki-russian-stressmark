from urllib import request, parse
from .russiangram_parser import RussiangramParser

def stressmark(s):
    data = { '__VIEWSTATE': '/wEPDwUKMTMzOTA3OTU5N2Rk5MNrzf8M72AYC/+c+xWZbzp8Td8=',
            '__VIEWSTATEGENERATOR': 'CA0B0334',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__EVENTVALIDATION': '/wEdAAMDOEAYUxkPEDCURzqp69xETjsDcGH04u5hS3jwIIl38e/d1Dv61Nm9xfklcqY855XV2JJyoBPZpaGFe8T+7UtRw3M4iA==',
            'ctl00$MainContent$UserSentenceTextbox': s,
            'ctl00$MainContent$SubmitButton': 'Annotate'}

    request_url = "https://russiangram.com/"
    encoded_data = parse.urlencode(data).encode()
    req = request.Request(request_url, data=encoded_data)
    resp = request.urlopen(req)
    body = resp.read()

    rgparser = RussiangramParser()
    rgparser.feed(str(body))
    return rgparser.data
