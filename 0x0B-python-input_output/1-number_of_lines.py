#!/usr/bin/python3
"""Number of lines """


def number_of_lines(filename=""):
    """return the number of lines"""
    with open(filename, "r", encoding="utf-8") as f:
        for i, l in enumerate(f):
            """"i for the count and l for run into function"""
            var = i + 1
        return var
