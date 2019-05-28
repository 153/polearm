import urllib.request as req
import urllib.parse as par
from urllib.request import Request
import json, base64
from config import *
from utils import *

regi = apiurl + "/apps"
auth = url + "oauth/authorize"
toke = url + "oauth/token"

def reg_app():
    app = {"client_name": "9pub",
           "redirect_uris": "urn:ietf:wg:oauth:2.0:oob",
           "scopes": ["read", "write"]}
    app = encode_data(app)
    return http_get(regi, app)

def get_auth_code(cid):
    data = {"scope": "read write",
            "response_type": "code",
            "redirect_uri": "urn:ietf:wg:oauth:2.0:oob",
            "client_id": cid}
    data = encode_data(data)
    print("?".join([auth, data.decode("ascii")]))

def get_token(cid, csec, code):
    data = {"client_id": cid,
            "client_secret": csec,
            "grant_type": "authorization_code",
            "redirect_uri": "urn:ietf:wg:oauth:2.0:oob",
            "code": code}
    data = encode_data(data)
    return http_get(toke, data)

def refresh_token(refresh, cid, csec):
    data = {"grant_type": "refresh_token",
            "refresh_token": refresh,
            "client_id": cid,
            "client_secret": csec}
    data = encode_data(data)
    print(http_get(toke, data))      

def register_wizard():
    client = json.loads(reg_app())
    cid, csec = client["client_id"], client["client_secret"]
    get_auth_code(cid)
    code = input("Input the code:\n> ")
    token = json.loads(get_token(cid, csec, code))

    for c in client:
        print(f"{c}: {client[c]}")
    for t in token.keys():
        print(f"{t}: {token[t]}")
    write_client(client)
    write_token(token)

def write_client(d):
    ctxt = [f"id {d['client_id']}",
            f"secret {d['client_secret']}"]
    ctxt = "\n".join(ctxt)
    with open("client.txt", "w") as c:
        c.write(ctxt)

def write_token(d):
    ttxt = ["access {d['access_token']}",
            f"refresh {d['refresh_token']}",
            f"created {d['created_at']}"]
    ttxt = "\n".join(ttxt)
    with open("token.txt", "w") as t:
        t.write(ttxt)
    
def load_client():
    with open("client.txt", "r") as c:
        c = c.read().splitlines()
    client = [line.split(" ")[1] for line in c]
    return client

def load_token():
    with open("token.txt", "r") as t:
        t = t.read().splitlines()
    token = [line.split(" ")[1] for line in t]
    return token
    
try:
    cid, csec = load_client()
except:
    register_wizard()
    cid, csec = load_client()
    
access, refresh = load_token()[:2]
