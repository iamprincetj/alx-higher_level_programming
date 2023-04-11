#!/usr/bin/python3
'''A module that contains a function called lookup'''


def lookup(obj):
    ''' The function that returns the list of available
        attributes and methods of an object
    Arguments:
        obj: the object to check
    Return: a list object
    '''

    return dir(obj)
