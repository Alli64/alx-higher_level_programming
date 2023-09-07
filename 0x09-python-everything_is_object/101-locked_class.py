#!/usr/bin/python3
"""Defines locked class"""


class LockedClass:
    """prevents user from creating new instance attributes
    except "first_name"."""
    __slots__ = ["first_name"]
