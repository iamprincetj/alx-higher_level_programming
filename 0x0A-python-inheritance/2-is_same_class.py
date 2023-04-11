#!/usr/bin/python3
''' A module that contains a function (is_same_class)'''


def is_same_class(obj, a_class):
    ''' A function that checks for an instance of classes
    Argument:
        obj: the object
        a_class: the class
    Return: True if the object is exactly an instance
        of the specified class ; otherwise False.
    '''

    return type(obj) == a_class
