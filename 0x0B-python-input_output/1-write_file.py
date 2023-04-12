#!/usr/bin/python3
'''A module that contains a function writes to a text file'''


def write_file(filename="", text=""):
    '''The function that write string to a text file
    Argument:
        filename: the file to write into
        text: the string to write in the file
    Return: the number of characters written
    '''

    with open(filename, 'w', encoding='utf-8') as fil:
        return fil.write(text)
