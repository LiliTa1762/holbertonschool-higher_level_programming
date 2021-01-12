#!/usr/bin/python3
"""Take in a URL, send a POST request and display a response"""


import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as t:
            sol = t.read()
            print(sol.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
