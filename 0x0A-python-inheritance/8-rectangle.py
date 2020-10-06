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
