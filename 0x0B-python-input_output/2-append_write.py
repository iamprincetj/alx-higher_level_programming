#!/usr/bin/python3
'''A module that contains a function that appends a string
    at the end of a text file'''


def append_write(filename="", text=""):
    '''The function that appends the string
    Arguments:
        filename: the file to append to
        text: the string to append
    Return: the number of characters
    '''

    with open(filename, 'a', encoding='utf-8') as fil:
        return fil.write(text)
