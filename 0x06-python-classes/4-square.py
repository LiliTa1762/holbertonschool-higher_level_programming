#!/usr/bin/python3
"""
Access and update private attribute
That would be: size
"""


class Square:
    """Define a private att"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    """Access and uptade private attribute"""
    @property
    def size(self):
        return(self.__size)

    """Access and uptade private attribute"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    """Define public instance method"""
    def area(self):
        return(self.__size ** 2)
