#!/usr/bin/python3
"""defines a class MyInt that inherits from int"""


class MyInt(int):
    """inverts == and != operators"""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
