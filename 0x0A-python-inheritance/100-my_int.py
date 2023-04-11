#!/usr/bin/python3
'''A module that contains class MyInt that inherits from int.'''


class MyInt(int):
    '''A class that inherits from int'''

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
