#!/usr/bin/python3
"""
Adds all arguments to a list
"""


import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = "add_item.json"
new_list = []
try:
    new_list = load_from_json_file(filename)
except FileNotFoundError:
    with open(filename, "w") as f:
        pass

if new_list:
    new_list += sys.argv[1:]
    save_to_json_file(new_list, filename)
else:
    save_to_json_file(sys.argv[1:], filename)
