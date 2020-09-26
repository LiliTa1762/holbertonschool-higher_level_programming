#!/usr/bin/python3
"""Function that prints a text"""


def text_indentation(text):
    """Every ., ?, : must be a 2 new lines after each of those"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    new_str = "".join([x if x not in ".?:" else x + "\n\n" for x in text])
    print("\n".join([x.strip() for x in new_str.split("\n")]), end="")
