#!/usr/bin/python3
'''A module that contain a class'''


class BaseGeometry:
    '''A class based on the previous classes'''

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
