#!/usr/bin/python3
"""
A class that inherits from other
"""


class MyList(list):
    """Subclass"""
    def __init__(self):
        """initializes the object"""
        super().__init__()
    def print_sorted(self):
        """Inherited by Superclass"""
        print(sorted(self))
