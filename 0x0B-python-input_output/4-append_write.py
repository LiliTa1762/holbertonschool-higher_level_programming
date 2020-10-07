#!/usr/bin/python3
"""
Function that appends a str at the end to a txt
"""


def append_write(filename="", text=""):
    """Append to a file"""
    with open(filename, "a+", encoding="utf-8") as f:
        return f.write(text)
