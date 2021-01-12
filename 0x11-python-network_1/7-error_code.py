#!/usr/bin/python3
"""Error code #1"""


import requests
import sys


if __name__ == "__main__":
    var = requests.get(sys.argv[1])
    if var.status_code <= 400:
        print("{}".format(var.text))
    else:
        print("Error code: {}".format(var.status_code))
