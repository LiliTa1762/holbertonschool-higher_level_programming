#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for x in a:
            if x != x - 1:
                print(x, end=" ")
            else:
                print(x, end="")
        print()
