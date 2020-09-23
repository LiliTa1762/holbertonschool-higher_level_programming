#!/usr/bin/python3
"""
Full coordination of a square
"""


class Square:
    """Define a private att"""
    def __init__(self, size=0, position=(0, 0)):
        """Define a private instance att"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if type(position) != tuple or len(position) != 2:
            raise TypeError(
               'position must be a tuple of 2 positive integers')
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError(
               'position must be a tuple of 2 positive integers')
        if position[0] < 0 or position[1] < 0:
            raise TypeError(
               'position must be a tuple of 2 positive integers')
        self.__position = position

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

    @property
    def position(self):
        """Access and uptade private attribute"""
        return(self.__position)

    @position.setter
    def position(self, value):
        """Access and uptade private attribute"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError(
               'position must be a tuple of 2 positive integers')
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError(
               'position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError(
               'position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Define public instance method"""
        return(self.__size ** 2)

    def my_print(self):
        """Define public instance method"""
        if self.__size > 0:
            for i in range(self.__position[1]):
                print()
            for s in range(self.__size):
                print((' ' * self.__position[0]) +
                      ('#' * self.__size))
        else:
            print("")
