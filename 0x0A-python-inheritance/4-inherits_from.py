#!/usr/bin/python3
''' A module that contains a function called inherits_from'''


def inherits_from(obj, a_class):
    ''' The function that checks for the instance of a class
    Arguments:
        obj: the object
        a_class: the class
    Returns: True if the object is an instance of a class that inherited
            otherwise False
    '''

    return isinstance(obj, a_class) and type(obj) != a_class
