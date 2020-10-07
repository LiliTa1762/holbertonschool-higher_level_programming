#!/usr/bin/python3
"""
Class with a public instance method
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of a square"""

    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Area method implemented"""
        return self.__size ** 2
