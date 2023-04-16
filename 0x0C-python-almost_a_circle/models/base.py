#!/usr/bin/python3
'''A module that cotains a base class'''
import json
import csv
import turtle


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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''A function that returns the JSON string representation
            of list_dictionaries'''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''A function that writes the JSON string representation
        of list_obj to a file'''
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as fil:
            if list_objs is None:
                fil.write("[]")
            else:
                my_list = [ln.to_dictionary() for ln in list_objs]
                fil.write(Base.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        '''A function that returns the list of the JSON string
        representation "json_string"'''
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''A function that returns an instance with
        all attributes already set'''
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                new_instance = cls(5)
            else:
                new_instance = cls(5, 5)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        '''A function that returns a list of instances'''
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as fil:
                my_list = Base.from_json_string(fil.read())
                return [cls.create(**dicts) for dicts in my_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''A function that serializes in CSV'''
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csv_fil:
            if list_objs is None or list_objs == []:
                csv_fil.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    format_csv = ["id", "width", "height", "x", "y"]
                else:
                    format_csv = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_fil, fieldnames=format_csv)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        '''A function that deserializes in CSV'''
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csv_fil:
                if cls.__name__ == "Rectangle":
                    format_csv = ["id", "width", "height", "x", "y"]
                else:
                    format_csv = ["id", "size", "x", "y"]
                my_list = csv.DictReader(csv_fil, fieldnames=format_csv)
                my_list = [dict([k, int(v)] for k, v in dicts.items())
                           for dicts in my_list]
                return [cls.create(**dicts) for dicts in my_list]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''A function that opens a window and
        draws all the Rectangles and Squares'''
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
