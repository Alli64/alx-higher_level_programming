#!/usr/bin/python3
"""takes in URL and email, sends POST request to the passed URL with the email
as parameter, and displays the body of the response (decoded in utf-8)"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    val = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(val).encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
