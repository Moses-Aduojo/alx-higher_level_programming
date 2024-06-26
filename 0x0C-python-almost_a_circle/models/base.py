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

    @staticmethod
    def from_json_string(json_string):
        """return the list of json string reprentation of an object"""
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an attribute with all instance already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        if dummy:
            """find out why **dictionary and not dictionary as in below"""
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load json representation fom file an create list of instances based
        the data
        """
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, "r") as file:
                data = file.read()
        except FileNotFoundError:
            return []

        dict_list = cls.from_json_string(data)

        instances_list = [cls.create(**dictionary) for dictionary in dict_list]
        return instances_list
