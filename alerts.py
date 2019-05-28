import urllib.request as req
import urllib.parse as par
from urllib.request import Request
import oauth, json, re, os
from config import *
from utils import *

adir = "./alerts/"

def index():
    route = apiurl + "/notifications"
    aindex = http_get(route, None, oauth.access)
    indexfn = adir + "index.json"
    with open(indexfn, "w", encoding="utf-8") as ind:
        ind.write(aindex)

def index2files():
    with open(adir+"index.json", "r", encoding="utf-8") as ind:
        ind = ind.read().encode("ascii", "xmlcharrefreplace")
    ind = json.loads(ind)
    latest = "0"
    
    for i in ind[::-1]:
        fn = adir + i["id"] + ".json"
        if not os.path.isfile(fn):
            with open(fn, "w") as alert_file:
                json.dump(i, alert_file)
        if int(i["id"]) > int(latest):
            latest = i["id"]
            print("\t  ".join([i["id"], i["type"], i["account"]["url"]]))
            if "status" in i.keys():
                con = strip_tags(i["status"]["content"])
                print("  " + con, "\n")

def refresh():
    index()
    index2files()
