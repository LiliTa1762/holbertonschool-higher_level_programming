#!/usr/bin/python3
"""Take in a URL, send a POST request and display a response"""


import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode()
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as rt:
        d = rt.read()
        print(d.decode('utf-8'))
