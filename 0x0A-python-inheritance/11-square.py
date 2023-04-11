#!/usr/bin/python3
'''A module that contains Square'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''The square class that inherits from Rectangle'''

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
