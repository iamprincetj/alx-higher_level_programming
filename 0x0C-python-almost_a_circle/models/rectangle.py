#!/usr/bin/python3
'''A module that contains a Rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''The Rectangle class which inherits from Base class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''returns the value of the width that was entered'''
        return self.__width

    @width.setter
    def width(self, value):
        '''to set the value yourself'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        '''returns the value of the height that was entered'''
        return self.__height

    @height.setter
    def height(self, value):
        '''to set the value yourself'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        '''returns the x entered'''
        return self.__x

    @x.setter
    def x(self, value):
        '''to set the value yourself'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        '''returns the value of y entered'''
        return self.__y

    @y.setter
    def y(self, value):
        '''to set the value yourself'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        '''returns the area of the rectangle'''
        return self.__height * self.__width

    def display(self):
        '''prints the pic of the rectangle with "#"'''
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print((" " * self.__x) + ("#" * self.__width))

    def __str__(self):
        x = self.__x
        y = self.__y
        wid = self.__width
        hei = self.__height
        return (f"[{type(self).__name__}] ({self.id}) {x}/{y} - {wid}/{hei}")

    def update(self, *args, **kwargs):
        '''A function that assigns an argument to each attribute'''
        if len(args) == 0:
            for k, v in kwargs.items():
                self.__setattr__(k, v)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]

        except IndexError:
            pass

    def to_dictionary(self):
        '''This function returns the dictionary representation of Rectangle'''
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'height': getattr(self, "height"),
                'width': getattr(self, "width")}
