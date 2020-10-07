#!/usr/bin/python3
"""
Function that reads n lines of a file
"""


def read_lines(filename="", nb_lines=0):
    """Read n lines"""
    with open(filename, "r", encoding="utf-8") as f:
        if nb_lines <= 0 or nb_lines >= nb_lines:
            a_read = f.read()
            print(a_read, end="")
