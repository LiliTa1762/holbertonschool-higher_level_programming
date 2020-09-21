#!/usr/bin/python3
def raise_exception():
    x = "hello"
    if not type(x) is int:
        raise TypeError("Only integers are allowed")
