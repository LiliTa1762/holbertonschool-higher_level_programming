#!/usr/bin/python3
"""POST an email with requests module"""


import requests
import sys


if __name__ == "__main__":
    payload = {'email': sys.argv2}
    r = requests.POST(sys.argv[1] data=payload)
    print(r.test)
