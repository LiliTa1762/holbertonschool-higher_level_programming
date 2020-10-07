#!/usr/bin/python3
"""
Function that reads a text file
"""


def read_file(filename=""):
    """Read a file"""
    with open(filename, "r", encoding="utf-8") as f:
        a_read = f.read()
        print(a_read, end="")
