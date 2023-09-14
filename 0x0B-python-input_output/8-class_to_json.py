#!/usr/bin/python3
"""defines python class to JSON function"""


def class_to_json(obj):
    """retun the dictionary representation of simple data structure"""
    return obj.__dict__
