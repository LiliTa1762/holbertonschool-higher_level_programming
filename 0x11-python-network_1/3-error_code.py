#!/usr/bin/python3
"""Display the response body and manage urllib.error.HTTPError exceptions"""


import urllib.request
import sys

re = urllib.request.Request(sys.argv[1])
try:
	with urllib.request.urlopen(re) as response:
		html = response.read()
		print(html.decode("utf-8"))
	except urllib.error.HTTPError as e:
		print("Error code: {}".format(e.code))
