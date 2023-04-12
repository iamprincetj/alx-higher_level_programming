#!/usr/bin/python3
'''A module that contains a function which reads file'''


def read_file(filename=""):
    '''The function that read file and output its contents to stdout
    Argument:
        filename: the file to be read
    '''

    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
