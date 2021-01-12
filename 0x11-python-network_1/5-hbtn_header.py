#!/usr/bin/python3
"""Take in a URL, send a request and display a value with requests"""


import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
