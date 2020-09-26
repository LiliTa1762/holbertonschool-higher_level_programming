#!/usr/bin/python3
"""Function that prints a square with the char #"""


def print_square(size):
    """Size must be an integer"""
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size is float and size < 0:
        raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")

    for s in range(size):
        for x in range(size):
            print("#", end="")
        print()
