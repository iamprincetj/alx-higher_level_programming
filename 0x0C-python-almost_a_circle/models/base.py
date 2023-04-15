#!/usr/bin/python3
'''A module that cotains a base class'''


class Base:
    '''The base class i was talking about
    this class is base/parent class of all the other classes
    in this particular project by Alx
    '''


    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialize a new Base.

        Argument:
            id : the id attribute
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
