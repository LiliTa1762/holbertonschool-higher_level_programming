#!/usr/bin/python3
"""
Base class
"""


import json


class Base:
    """Representation of a base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation part"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Static method, returns the JSON representation"""
        if list_dictionaries is None:
            return("[]")
        else:
            return json.dumps(list_dictionaries)
