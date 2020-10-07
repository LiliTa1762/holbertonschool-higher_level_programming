#!/usr/bin/python3
"""
Function that reads n lines of a file
"""


def read_lines(filename="", nb_lines=0):
    """Read n lines"""
    with open(filename, "r", encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
            return

        for i, x in enumerate(f):
            if i == nb_lines:
                break
            print(x, end="")
