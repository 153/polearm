import urllib.request as req
import urllib.parse as par
from urllib.request import Request
import json, base64, re

def encode_data(data):
    return par.urlencode(data).encode('ascii')

def http_get(website, data=None, access=None):
    if data is 1:
        data = encode_data({})
    if access:
        website = Request(website)
        website.add_header("Authorization", "Bearer " + access)
    with req.urlopen(website, data) as page:
        page = page.read().decode("utf-8", "xmlcharrefreplace")
    return page

def strip_tags(msg):
    return re.sub('<[^<]+>', "", msg)
