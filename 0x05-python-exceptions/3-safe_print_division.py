#!/usr/bin/python3
def safe_print_division(a, b):
    r = 0
    try:
        r = a / b
        return (r)
    except ZeroDivisionError:
        r = None
    finally:
        print("Inside result: {}".format(r))
        return (r)
