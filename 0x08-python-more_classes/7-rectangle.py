#!/usr/bin/python3
'''A module that contain a rectange class with width and height
    and check for the area and perimeter
'''


class Rectangle:
    '''A class that represent a rectangle
    arguments:
         width: how long is the rectangle?
         height: how tal is it?
         Return: the string of rectange
    '''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 and self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        str_1 = ""
        if self.__width == 0 or self.__height == 0:
            return str_1
        for i in range(self.__height):
            for j in range(self.__width):
                str_1 += str(self.print_symbol)
            if i is not self.__height - 1:
                str_1 += "\n"
        return str_1

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
