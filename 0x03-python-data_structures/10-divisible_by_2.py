#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    for i in range(len(my_list)):
        if my_list[i] % 2:
            new_list[i] = 0
        else:
            new_list[i] = 1
    return new_list
