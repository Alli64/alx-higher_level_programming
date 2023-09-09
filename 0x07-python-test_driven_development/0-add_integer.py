#!/usr/bin/python3
"""defines integer addition function"""


def add_integer(a, b=98):
    """return the integer addition of a and b"""
    if ((not isinstance(a, int) andnot isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
