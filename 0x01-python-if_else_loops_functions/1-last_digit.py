#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Finding the last digit
l_dgt = (number % 10)
if (number < 0 and l_dgt != 0):
    l_dgt = l_dgt - 10
    print("Last digit of", number, "is", l_dgt, "and is less than 6 and not 0")
if (l_dgt > 5):
    print("Last digit of", number, "is", l_dgt, "and is greater than 5")
elif (l_dgt == 0):
    print("Last digit of", number, "is", l_dgt, "and is 0")
