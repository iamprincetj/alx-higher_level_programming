#!/usr/bin/python3
'''A module that contain a Rectangle function'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''this class represents a rectangle using BaseGeometry'''

    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        str1 = "[" + str(self.__class__.__name__) + "] "
        str1 += str(self.__width) + "/" + str(self.__height)
        return str1
