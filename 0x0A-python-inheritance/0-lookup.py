#!/usr/bin/python3
'''A module that contains a class called lookup'''


def lookup(obj):
    ''' The class  that returns the list of available
        attributes and methods of an object
    Arguments:
        obj: the object to check
    Return: a list object
    '''

    return dir(obj)
