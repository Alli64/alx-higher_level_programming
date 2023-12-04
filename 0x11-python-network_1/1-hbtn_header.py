#!/usr/bin/python3
"""takes in a URL sends request to the URL and displays value X-R-id"""

import sys
import urllib.request

if __name__ == "__main__":

    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
