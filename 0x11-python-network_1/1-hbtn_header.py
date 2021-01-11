#!/usr/bin/python3
"""Take in a URL, send a request and displaya value"""


import urllib.request
import sys


if __name__ == "__main__":
	with urllib.request.urlopen(sys.argv[1]) as response:
		html = response.read()
		print(response.getheader("X-Request-Id"))
