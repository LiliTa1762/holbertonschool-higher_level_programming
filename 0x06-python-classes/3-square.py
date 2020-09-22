#!/usr/bin/python3
"""
Define a private instance attribute
That would be: area
"""


class Square:
    """Define a private att"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    """Define public instance method"""
    def area(self):
        return(self.__size ** 2)
