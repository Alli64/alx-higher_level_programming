#!/usr/bin/python3
"""defines a function that adds attribute to object if possible"""


def add_attribute(obj, attr, value):
    """add new attribute to an object if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
