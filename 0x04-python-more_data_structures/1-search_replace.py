#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    new_list = [replace if x == search else x for x in my_list]
    return new_list
