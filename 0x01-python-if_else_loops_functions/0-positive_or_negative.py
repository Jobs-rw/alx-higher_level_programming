#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print('{} is '.format(number), end='')
if number < 0:
    print("is negative number")
elif number == 0:
    print("is zero")
else:
    print("is positive number")