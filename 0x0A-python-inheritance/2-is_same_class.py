#!/usr/bin/python3
"""defines a class-checking function"""


def is_same_class(obj, a_class):
    """check if the object is exactly an instance of the specified class"""
    if type(obj) == a_class:
        return True
    return False
