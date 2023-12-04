#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and uses the GitHub
API to display your id"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: script.py <user> <token>")
        sys.exit(1)

    url = "https://api.github.com/user"
    user = sys.argv[1]
    token = sys.argv[2]
    auth = (user, token)

    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        git_id = response.json().get("id")
        print(f"Github Id: {git_id}")
    else:
        print(f"Error: {response.status_code}, {response.text}")
