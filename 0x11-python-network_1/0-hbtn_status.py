#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

import urllib.request


if _name_ == "__main__":

    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        web = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(web)))
        print("\t- content: {}".format(web))
        print("\t- utf8 content: {}".format(web.decode('UTF-8')))
