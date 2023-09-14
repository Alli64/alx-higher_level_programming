#!/usr/bin/python
"""defines a function that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """return the python object representation of JSON string"""
    return json.loads(my_str)
