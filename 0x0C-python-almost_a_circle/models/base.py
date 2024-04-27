#!/usr/bin/python3
"""
This module define base class for rectangle class
"""


import json


class Base:
    """
    this is the Base class provide attrinute and methods for a
    rectangle
    """
    __nb_objects = 0

    """
    intitializes public instance attribute
    """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json list representaion of list_dictionary
        parameter: list_dictionaries - a list of dictionary
        """
        print(type(list_dictionaries))
        print(list_dictionaries)
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []

        """construct file name"""
        class_name = cls.__name__
        filename = "{}.json".format(class_name)

        """get dictionary representation of object"""
        dict_list = [(obj.to_dictionary()) for obj in list_objs]

        """convert to json string"""
        json_string = cls.to_json_string(dict_list)

        """save to file named filename"""
        with open(filename, 'w') as file:
            file.write(json_string)
