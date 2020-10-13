#!/usr/bin/python3
"""
Base class
"""


import json


class Base:
    """Representation of a base"""
    __nb_objects = 0

    @classmethod
    def load_from_file(cls):
        """A list of instances"""
        filename = cls.__name__ + ".json"
        lst = []
        try:
            with open(filename, "r", enconding="utf-8") as f:
                lst = cls.from_json_string(f.read())
            for i, x in enumerate(lst):
                lst[i] = cls.create(**lst[i])
        except:
            pass
        return lst

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all att"""
        if (cls.__name__ == "Rectangle"):
            dummy = cls(1, 1)
        elif (cls.__name__ == "Square"):
            dummy = cls(1)
        dummy.update(**dictionary)
        return(dummy)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string rep"""
        if json_string is None:
            return ("[]")
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string rep of a list to a file"""
        filename = cls.__name__ + ".json"
        list_empty = []
        if list_objs is not None:
            for i in list_objs:
                list_empty.append(cls.to_dictionary(i))
        with open(filename, "w", encoding="utf-8") as f:
                f.write(cls.to_json_string(list_empty))

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method, returns the JSON representation"""
        if list_dictionaries is None:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    def __init__(self, id=None):
        """Instantiation part"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
