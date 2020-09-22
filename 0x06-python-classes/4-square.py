#!/usr/bin/python3
"""
Access and update private attribute
That would be: size
"""


class Square:
    """Define a private att"""
    def __init__(self, size=0):
        """Define a private att"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """Access and uptade private attribute"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """Access and uptade private attribute"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Define public instance method"""
        return(self.__size ** 2)
