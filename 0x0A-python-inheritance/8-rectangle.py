#!/usr/bin/python3
"""
Class with a public instance method
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
