#!/usr/bin/python3
"""takes in a URL sends request to the URL and displays value of X-Request-Id"""

import sys
imporrt urllib.request

if __name__ == "__main__":

    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers.get("X-Request-Id"))
