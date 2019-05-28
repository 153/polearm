import urllib.request as req
import urllib.parse as par
from urllib.request import Request
import oauth, json, re, os
from config import *
from utils import *

# collect:     dirs       --> #hash, #hash, #hash ...
# track:       #hash      --> index.json
# index2files: index.json --> status.json, status.json ... 
# index2dirs:  index.json --> status(flakeid) [index, context, reblog_by, etc etc]

tdir = "./tag/"

def init():
    if not os.path.isdir(tdir):
        os.mkdir(tdir)

def collect():
    tags = os.listdir(tdir)
    return tags

def track(tname):
    hdir = tdir + tname
    hfn = "index.json"
    hurl = apiurl + "/timelines/tag/" + tname
    hindex = http_get(hurl, None, oauth.access)
    if not os.path.isdir(hdir):
        os.mkdir(hdir)
    with open(hdir + "/" + hfn, "w", encoding="utf-8") as fi:
        fi.write(hindex)

def index2files(tname):
    hdir = tdir + tname
    hindex = hdir + "/index.json"
    with open(hindex, "r", encoding="utf-8") as ind:
        ind = ind.read().encode("ascii", "xmlcharrefreplace")
    ind = json.loads(ind)

    for n, i in enumerate(ind):
        fn = hdir + "/" + i['id'] + ".json"
        if not os.path.isfile(fn):
            with open(fn, "w") as tweet:
                json.dump(i, tweet)

def multi_track(tags=[]):
    if not tags:
        tags = ["pleroma", "slackware", "drugs"]
    for t in tags:
        track(t)
        index2files(t)
