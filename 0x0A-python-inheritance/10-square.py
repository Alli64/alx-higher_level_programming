#!/usr/bin/python3
"""defines a Rectangle, subclass Sqaure"""
rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """represent square"""

    def __init__(self, size):
        """initialize square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
