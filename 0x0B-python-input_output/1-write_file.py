#!/usr/bin/python3
"""defines  a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """write a string to UTF8 text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
