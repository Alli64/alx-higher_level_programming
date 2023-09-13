#!/usr/bin/python3
"""defines a class and inherited class_checking function"""


def is_kind_of_class(obj, a_class):
    """check if object is instance of, or instnace of a class inherited from"""
    if isinstance(obj, a_class):
        return True
    return False
