#!/usr/bin/python3
"""defines a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends string to the end of text file UTF8"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
