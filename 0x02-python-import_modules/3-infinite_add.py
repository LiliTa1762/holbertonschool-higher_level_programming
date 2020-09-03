#!/usr/bin/python3
import sys
add = 0
# Getting the length of command
n = len(sys.argv)
for i in range(1, n):
    add += int(sys.argv[i])
print(add)
