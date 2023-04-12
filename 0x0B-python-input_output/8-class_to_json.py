#!/usr/bin/python3
'''A module that contains a function'''


def class_to_json(obj):
    '''The function that 
    Argument: obj: the object
    Return: the dictionary description with simple data structure
    '''
    return obj.__dict__
