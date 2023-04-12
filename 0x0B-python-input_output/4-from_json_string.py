#!/usr/bin/python3
'''A module that contains a function that does json stuff'''
import json


def from_json_string(my_str):
    '''The function that does the json stuff
    Argument: my_str: the obj
    '''

    return json.loads(my_str)
