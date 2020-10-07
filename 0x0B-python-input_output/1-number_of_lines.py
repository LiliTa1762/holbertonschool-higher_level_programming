#!/usr/bin/python3
"""Number of lines """


def number_of_lines(filename=""):
    """return the number of lines"""
    with open(filename, "r", encoding="utf-8") as f:
        i = 0
        for i, l in enumerate(f):
            """"i for the count and l for run into function"""
            i += 1
        return i
