#!/usr/bin/python3
"""
Define a private instance attribute
That would be: area
"""


class Square:
    def __init__(self, size=0):
    """Define a private att"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
    """Define public instance method"""
        return(self.__size ** 2)
