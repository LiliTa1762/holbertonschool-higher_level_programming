#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
# Argv is 0 (whithout the name of the file)
if (len(argv) == 1):
    print((len(argv) - 1), "arguments.")
# Argv is 1
elif (len(argv) == 2):
    print((len(argv) - 1), "argument: ")
else:
    print((len(argv) - 1), "arguments: ")
for i in range(1, len(argv)):
    print("{}: {}".format(i, argv[i]))
