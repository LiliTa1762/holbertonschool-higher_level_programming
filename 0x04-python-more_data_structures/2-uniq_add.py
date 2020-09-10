#!/usr/bin/python3
def uniq_add(my_list=[]):
    plus = 0
    for x in set(my_list):
        plus += x
    return plus
