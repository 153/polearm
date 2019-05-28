import urllib.request as req
import urllib.parse as par
from urllib.request import Request
import oauth, json, re, os
from config import *
from utils import *

udir = "./users/"

def init():
    if not os.path.isdir(udir):
        os.mkdir(udir)

def collect():
    users = os.listdir(udir)
    return users

def flake2user(flake=''):
    if not flake:
        return None
    uurl = apiurl + "/accounts/" + flake
    user = json.loads(http_get(uurl, None, oauth.access)\
                      .encode("ascii", "xmlcharrefreplace"))
    user = {"flake": flake, "un": "@" + user["acct"],
            "url": user["url"], "name": user["display_name"]}    
    print("\n".join([user["flake"], user["un"],
                     user["url"], user["name"], ""]))
    return user

def flakedb(op=None, user=None):
    print("")

def stalk(user):
    return user

def mkuser(flake):
    # turn flake into userdir;
    # create index, followers, following, statuses)
    # grow flake-user db with ( flake : url ) 
    uudir = udir + flake
    uurl = apiurl + "/accounts/" + flake
    if not os.path.isdir(uudir):
        os.mkdir(uudir)
    files = {"index": "",
             "followers": "/followers",
             "following": "/following",
             "statuses": "/statuses"}
    for f in files.keys():
        fn = uudir + "/" + f + ".json"
        data = http_get(uurl + files[f], None, oauth.access)
        with open(fn, "w", encoding="utf-8") as fi:
            fi.write(data)
            
#flake2user("9hFbvWZAt3QjuuEQ1A") # jeff
#flake2user("9inmVh7tAbOnvoDpQG") # sum
# 9iHMnJOJL9wPfEvRtA ffs
# 9iF6wdOHiNjpCDnLAu kaniini
#flake2user("9iGFHkjlEuh6N90G8W") # a_breaking_glass
#flake2user("9ipDrIqZ0r5MvBbf3w") # orekix

names = ["9inmVh7tAbOnvoDpQG",
         "9iHMnJOJL9wPfEvRtA",
         "9iF6wdOHiNjpCDnLAu",
         "9iFkxvyUke6UoCWpXs"]         

for account in names:
    flake2user(account)

#mkuser("9inmVh7tAbOnvoDpQG")
