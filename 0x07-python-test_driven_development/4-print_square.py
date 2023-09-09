#!/usr/bin/python3
"""defines a function that prints square"""


def print_square(size):
    """print square with #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
