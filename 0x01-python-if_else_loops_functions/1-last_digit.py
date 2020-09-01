#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lst_dg = (number % 10) + 0
if (lst_dg > 5):
    print("Last digit of", number, "is", lst_dg, "and is greater than 5")
elif (lst_dg == 0):
    print("Last digit of", number, "is", lst_dg, "and is 0")
else:
    print("Last digit of", number, "is", lst_dg, "and is less than 6 and not 0")
