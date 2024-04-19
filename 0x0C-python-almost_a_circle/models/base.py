#!/usr/bin/python3
'''Defines a Base model class.'''
import json
import csv
import turtle


class Base():
    '''Represent a base model.

    Attribute:
       __nb_objects (): The number of instantiated bases.
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialize a new base.

        Args:
           id (int): The identity of a new base.
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def from_json_string(json_string):
        '''Returns the list of the JSON string representation json_string.

        Args:
           json_string (str): A string representing a list f dictionaries.
        '''
        if json_string is None or json_string == '[]':
            return []
        return json.loads(json_string)


    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns the JSON string representation of list_dictionaries.

        Args:
           list_dictionaries (list): A list of dictionaries.
        '''
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances.'''
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, 'r') as myfile:
                list_dict = Base.from_json_string(myfile.read())
                return [cls.create(**dic) for dic in list_dict]
        except IOError:
            return []
    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes the JSON string representation of list_objs to a file.

        Args:
           cls (obj): Classes.
           list_objs (list): A list of instances who inherits of Base.
        '''
        filename = cls.__name__ + ".json"
        with open(filename, "w") as myfile:
            if list_objs is None:
                myfile.write("[]")
            else:
                list_dict = [op.to_dictionary() for op in list_objs]
                myfile.write(Base.to_json_string(list_dict))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Write the csv serializtion of a list of objects.

        Args:
           list_objs (list): A list of inherited Base instance.
        '''
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as myfile:
            if list_objs is None or list_objs == []:
                myfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(myfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        '''Return a list of classes instantiated fro a csv file.'''
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []


