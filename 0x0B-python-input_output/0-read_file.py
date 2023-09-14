#!/usr/bin/python3
"""defines a function that reads a text file"""


def read_file(filename=""):
    """prints contents of text file UTF8 to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
