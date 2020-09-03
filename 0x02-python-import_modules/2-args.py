#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    # No aguments
    if len(argv[1:]) == 0:
        print("{} arguments.".format(len(argv[1:])))
    # Only one arguments
    elif len(argv[1:]) == 1:
        print("{} argument:".format(len(argv[1:])))
    else:
        print("{} arguments:".format(len(argv[1:])))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
