import urllib.request as req
import urllib.parse as par
from urllib.request import Request
import time
import oauth
import alerts, tags
from config import *
from utils import *

def api2disk(acc, route, nick):
    route = apiurl + route
    nick = "./test/" + nick + ".json"
    data = http_get(route, None, acc)

    with open(nick, "w", encoding="utf-8") as fi:
        fi.write(data)

targets = [
    ["/timelines/tag/pleroma", "hash-pleroma"],
    ["/instance", "info"],
    ["/accounts/verify_credentials", "self"],
    ["/notifications", "alerts"],
    ["/timelines/public", "public"],
    ["/timelines/home", "home"]
    ]

while True:
    try:
        alerts.refresh()
        tags.multi_track()
    except:
        pass
    time.sleep(300)

#for t in targets:
#    api2disk(oauth.access, t[0], t[1])


# hello = {"status": "I see.",
#          "visibility": "unlisted"}
# hello = encode_data(hello)
# postu = apiurl + "/statuses"
# http_get(postu, hello, oauth.access)


# api2disk(oauth.access, "/accounts/verify_credentials", "self")
# api2disk(oauth.access, "/accounts/32779", "self-info")
# api2disk(oauth.access, "/accounts/32779/statuses", "self-statuses")
# api2disk(oauth.access, "/accounts/32779/following", "self-following")

def user_verb(user, verb, opt=None):
#    useru = apiurl + "/accounts/" + user
    useru = "/".join([apiurl, "accounts", user, verb])
    http_get(useru, 1)

# useru = apiurl + "/accounts/"
# for user in ["10981"]:
#     useru = useru + user + "/unfollow"
#     print(useru)
#     confirm = encode_data({})
#     http_get(useru, confirm, oauth.access)
