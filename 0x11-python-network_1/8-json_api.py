#!/usr/bin/python3
"""takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
import sys

if __name__ == "__main__":
    try:
        letter = sys.argv[1]
    except:
        letter = ""
    req = requests.post("http://0.0.0.0:5000/search_user" data={'q': letter})
    try:
        print("[{}] {}".format(req.json()['id'], req.json()['name']))
    except ValueError:
        print("Not a valid JSON")
    except:
        print("No result")
