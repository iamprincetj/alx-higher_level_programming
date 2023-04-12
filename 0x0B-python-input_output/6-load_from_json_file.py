#!/usr/bin/python3
'''A module that contains a function that
    creates an Object from a “JSON file'''
import json


def load_from_json_file(filename):
    '''The function that  creates an Object from a “JSON file
    Argument: filename: the file 
    '''

    with open(filename) as fil:
        return json.load(fil)
