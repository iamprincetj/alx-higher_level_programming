#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number1 = abs(number) % 10
if number < 0:
    number1 *= -1
if number1 > 5:
    print(f"Last digit of {number:d} is {number1:d} and is greater than 5")
elif number1 < 6 and number1 != 0:
    print(f'Last digit of {number:d} '
          f'is {number1:d} and is less than 6 and not 0')
else:
    print(f"Last digit of {number:d} is {number1:d} and is 0")
