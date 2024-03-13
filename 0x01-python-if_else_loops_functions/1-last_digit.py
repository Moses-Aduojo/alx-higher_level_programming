#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_number = abs(number)
lastdigit = abs_number % 10
sign = "-" if number < 0 and lastdigit != 0 else ""

if lastdigit > 5:
    print(f"Last digit of {number} is {sign}{lastdigit} and is greater than 5")
elif lastdigit < 6 and lastdigit != 0:
    print(f"Last digit of {number} is {sign}{lastdigit} and is less than 6\
    and not 0")
else:
    print(f"Last digit of {number} is {sign}{lastdigit} and is 0")
