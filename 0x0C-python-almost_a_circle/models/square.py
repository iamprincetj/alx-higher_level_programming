#!/usr/bin/python3
'''A module that contains a class named Square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A class that defines a square which inherits from Rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''returns the updated value for size'''
        return self.width

    @size.setter
    def size(self, value):
        '''A function that sets the value of size'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        '''Update __str__ function for square'''
        x = self.x
        y = self.y
        wid = self.width
        return (f"[{type(self).__name__}] ({self.id}) {x}/{y} - {wid}")

    def update(self, *args, **kwargs):
        '''A function that updates the update function from Rectangle'''
        if len(args) == 0:
            for k, v in kwargs.items():
                self.__setattr__(k, v)
            return
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        '''This function returns the dictionary representation of square'''
        return {'id': getattr(self, "id"), 'x': getattr(self, "x"),
                'size': getattr(self, "size"), 'y': getattr(self, "y")}
