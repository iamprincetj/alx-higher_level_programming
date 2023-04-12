#!/usr/bin/python3
'''A module that contains a function that does JSON'''
import json


def to_json_string(my_obj):
    '''The function that the JSON representation of an object
    Argument: my_obj: the obj to represent with JSON
    Return: the representation of the obj in JSON
    '''

    return json.dumps(my_obj)
