#!/usr/bin/python3
"""
Class with a public instance method
"""


class BaseGeometry:
    """Class with a public instance method"""

    def area(self):
        """Public instance method"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''
        Next public instance method
        '''
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''
    Subclass.
    '''

    def __init__(self, width, height):
        '''
        initialization with two arg.
        '''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area method implemented for rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """str implemented"""
        return("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))


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

    def __str__(self):
        """str implemented for a square"""
        return("[Square] {:d}/{:d}".format(self.__size, self.__size))
