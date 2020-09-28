#!/usr/bin/python3
"""Define a Rectangle"""


class Rectangle:
    """Class Rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiation object"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Define setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Define height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Define setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Define area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Define Perimeter of rentangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """Prints the rectangle with a char"""
        string = ""
        if self.__width != 0 or self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """To be able to recreate a new instance"""
        return "Rectangle ({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """When an instance of the class is deleted"""
        print("Bye rectangle...")
