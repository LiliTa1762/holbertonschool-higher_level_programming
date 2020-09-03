#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
# Getting the length of command
n = len(sys.argv)
for i in range(1, n):
    add += int(sys.argv[i])
print(add)
