#!/usr/bin/python3
''' A module that contains module called (is_kind_of_class)'''


def is_kind_of_class(obj, a_class):
    ''' The function that check for the an instance of
        object
    Arguments:
        obj: the object to check
        a_class: the class to check
    Returns: True if the object is an instance of, or if the object
        otherwise False
    '''

    return isinstance(obj, a_class)
