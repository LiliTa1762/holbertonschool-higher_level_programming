#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    # No arguments
    if (len(argv) == 1):
        print("{} arguments. ".format(len(argv) - 1))
    # Only one argument
    elif (len(argv) == 2):
        print("{} argument: ".format(len(argv) - 1))
    else:
        print("{} arguments: ".format(len(argv) - 1))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
