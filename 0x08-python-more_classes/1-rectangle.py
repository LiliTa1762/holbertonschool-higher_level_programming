#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Class with private instance att"""
    def __init__(self, width=0, height=0):
        """Instantiation object"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve a property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set if this conditions"""
        if type(width) is not int:
            raise TypeError("width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieve a property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set if this conditions"""
        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
