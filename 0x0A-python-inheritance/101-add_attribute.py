#!/usr/bin/python3
'''A module that contains a function that adds attributes to objects.'''


def add_attribute(obj, att, value):
    '''Add a new attribute to an object if possible.
    Args:
        obj (any): The object
        att (str): The name
        value (any): The value
    Raises:
        TypeError: If the attribute cannot be added.
    '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
