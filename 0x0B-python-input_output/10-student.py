#!/usr/bin/python3
'''A module that contains a class named Student but this time modified'''


class Student:
    '''The class that define a student like the prev student
        but modified
    '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (type(attrs) == list and
                all(type(tin) == str for tin in attrs)):
            return {ky: getattr(self, ky)for ky in attrs if hasattr(self, ky)}
        return self.__dict__
