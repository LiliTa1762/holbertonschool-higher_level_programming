#!/usr/bin/python3
"""
From JSON string to object
"""


import json


def from_json_string(my_str):
    """Returns an object represented by JSON"""
    return json.loads(my_str)
