#!/usr/bin/python3
'''A module that contain a square function'''


def print_square(size):
    '''A function that prints a square with "#" character
       arguments:
            size: the length of the square
        Return: None
    '''

    msg = "size must be an integer"
    if not isinstance(size, int):
        raise TypeError(msg)
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError(msg)
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
