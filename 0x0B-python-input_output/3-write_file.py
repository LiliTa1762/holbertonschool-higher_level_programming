#!/usr/bin/python3
"""
Function that writes a str to a txt
"""


def write_file(filename="", text=""):
    """Write a string"""
    with open(filename, "w", encoding="utf-8") as f:
        s = str(text)
        return(f.write(s))
