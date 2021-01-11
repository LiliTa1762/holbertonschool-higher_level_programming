#!/usr/bin/python3
"""Fetch a webpage and retrieve some data"""


import requests


if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')
    """html = response.decode("UTF-8")"""
    print("Body response:")
    print("\t- type: {}".format(type('__class__')))
    print("\t- content: {}".format(response.text))
