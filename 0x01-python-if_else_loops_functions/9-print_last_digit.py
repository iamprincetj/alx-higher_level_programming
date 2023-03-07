#!/usr/bin/python3

def print_last_digit(number):
    if number >= 0:
        num1 = number % 10
    else:
        num1 = number % -10
        num1 *= -1
    print("{:d}" .format(num1), end="")
    return num1
