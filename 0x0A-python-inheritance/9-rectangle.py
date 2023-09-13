#!/usr/bin/python3
"""define a class Rectangle that inherits from BaseGeometry"""
Base Geometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """represents rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """initialize a rectangle"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """return area"""
        return self.__width * self.__height

    del __str__(self):
        """return print() and str() represantation of rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
